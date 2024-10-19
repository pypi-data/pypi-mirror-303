import json
from langchain_openai import ChatOpenAI
from .agent import run_agent, Runnable, INPUT_MESSAGE, output
import asyncio
from langchain_core.messages import HumanMessage
from pycoze import utils
from pycoze.access.tool_for_bot import import_tools

params = utils.arg.read_params_file()
llm_file = params["appPath"] + "/JsonStorage/llm.json"


def load_role_setting(bot_setting_file: str):
    with open(bot_setting_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_tools(bot_setting_file: str):
    with open(bot_setting_file, "r", encoding="utf-8") as f:
        role_setting = json.load(f)

    tools = []
    for tool_id in role_setting["tools"]:
        tools.extend(import_tools(tool_id))
    return tools


def agent_chat(bot_setting_file, history):
    role_setting = load_role_setting(bot_setting_file)
    tools = load_tools(bot_setting_file)
    with open(llm_file, "r", encoding="utf-8") as f:
        cfg = json.load(f)
        chat = ChatOpenAI(
            api_key=cfg["apiKey"],
            base_url=cfg["baseURL"],
            model=cfg["model"],
            temperature=(
                role_setting["temperature"] * 2
                if cfg["model"].startswith("deepseek")
                else role_setting["temperature"]
            ),
            stop_sequences=[
                "tool▁calls▁end",
                "tool▁call▁end",
            ],  # 停用deepseek的工具调用标记，不然会虚构工具调用过程和结果
        )
    prompt = role_setting["prompt"]
    if cfg["model"].startswith("deepseek") and len(tools) > 0:
        prompt += """
如果需要调用工具，请使用以正确的json格式进行结尾（务必保证json格式正确，不要出现反斜杠未转义等问题）：
```json
{"name": 函数名, "parameters": 参数词典}
```
"""
    agent = Runnable(
        agent_execution_mode=(
            "ReAct" if cfg["model"] in ["command-r"] else "FuncCall"
        ),  # 'FuncCall' or 'ReAct'，大模型支持FuncCall的话就用FuncCall
        tools=tools,
        llm=chat,
        assistant_message=prompt,
    )
    return asyncio.run(run_agent(agent, history))


def chat(bot_setting_file: str):
    history = []
    while True:
        input_text = input()
        if not input_text.startswith(INPUT_MESSAGE):
            raise ValueError("Invalid message")
        message = json.loads(input_text[len(INPUT_MESSAGE) :])
        history.append(HumanMessage(message["content"]))
        result = agent_chat(bot_setting_file, history)
        history.append(output("assistant", result))


def get_chat_response(bot_setting_file: str, input_text: str):
    history = [HumanMessage(input_text)]
    result = agent_chat(bot_setting_file, history)
    return result
