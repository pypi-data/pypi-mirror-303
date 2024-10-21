import asyncio
import json
from langchain_openai import ChatOpenAI
from .chat import info
from .assistant import Runnable
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    AIMessageChunk,
    SystemMessage,
)
from langchain_core.agents import AgentFinish


async def run_agent(agent, inputs: list):
    if agent.agent_execution_mode == "FuncCall":
        exist_ids = set()
        content_list = []
        async for event in agent.astream_events(inputs, version="v2"):
            kind = event["event"]
            if kind == "on_chain_end":
                if "data" in event:
                    if (
                        "output" in event["data"]
                        and event["data"]["output"] == "end"
                        and "input" in event["data"]
                        and isinstance(event["data"]["input"], list)
                    ):
                        input_list = event["data"]["input"]
                        for msg in input_list:
                            if isinstance(msg, HumanMessage) or isinstance(
                                msg, SystemMessage
                            ):
                                content_list = []
                            if isinstance(msg, AIMessage) and not isinstance(
                                msg, AIMessageChunk
                            ):
                                content = msg.content
                                if content:
                                    content_list.append(content)
            elif kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    info("assistant", content)
            elif kind == "on_chain_start":
                data = event["data"]
                if "input" in data:
                    input_list = (
                        data["input"]
                        if isinstance(data["input"], list)
                        else [data["input"]]
                    )
                    if len(input_list) == 0:
                        continue
                    msg = input_list[-1]
                    if isinstance(msg, AIMessage) and not isinstance(
                        msg, AIMessageChunk
                    ):
                        if "tool_calls" in msg.additional_kwargs:
                            tool_calls = msg.additional_kwargs["tool_calls"]
                            for t in tool_calls:
                                if t["id"] in exist_ids:
                                    continue
                                exist_ids.add(t["id"])
                                tool = t["function"]["name"]
                                info("assistant", f"\n[调用工具:{tool}]\n\n")

        return "\n".join(content_list)
    else:
        assert agent.agent_execution_mode == "ReAct"
        inputs_msg = {"input": inputs[-1].content, "chat_history": inputs[:-1]}
        use_tools = []
        async for event in agent.astream_events(inputs_msg, version="v2"):
            kind = event["event"]
            result = None
            if kind == "on_chain_end":
                if "data" in event:
                    if "output" in event["data"]:
                        output = event["data"]["output"]
                        if "agent_outcome" in output and "input" in output:
                            outcome = output["agent_outcome"]
                            if isinstance(outcome, AgentFinish):
                                result = outcome.return_values["output"]
            elif kind == "on_tool_start":
                use_tools.append(event["name"])
                info("assistant", f"\n[调用工具:{use_tools}]\n\n")
        return result


if __name__ == "__main__":
    from langchain_experimental.tools import PythonREPLTool

    llm_file = r"C:\Users\aiqqq\AppData\Roaming\pycoze\JsonStorage\llm.json"
    with open(llm_file, "r", encoding="utf-8") as f:
        cfg = json.load(f)
        chat = ChatOpenAI(
            api_key=cfg["apiKey"],
            base_url=cfg["baseURL"],
            model=cfg["model"],
            temperature=0,
        )
    python_tool = PythonREPLTool()
    agent = Runnable(
        agent_execution_mode="FuncCall",  # 'FuncCall' or 'ReAct'，大模型支持FuncCall的话就用FuncCall
        tools=[python_tool],
        llm=chat,
        assistant_message="请以女友的口吻回答，输出不小于100字，可以随便说点其他的",
    )

    inputs = [HumanMessage(content="计算根号7+根号88")]
    print(asyncio.run(run_agent(agent, inputs)))
