import json
from langchain_core.messages import AIMessage


INPUT_MESSAGE = "INPUT_MESSAGE=>"
_OUTPUT_MESSAGE = "OUTPUT_MESSAGE=>"
_INFOMATION_MESSAGE = "INFOMATION_MESSAGE=>"
_LOG = "LOG=>"


def log(content, *args, end="\n", **kwargs):
    print(_LOG + content, *args, end=end, **kwargs)


def output(role, content):
    assert role == "assistant"
    print(_OUTPUT_MESSAGE + json.dumps({"role": role, "content": content}))
    return AIMessage(content=content)


def info(role, content):
    print(_INFOMATION_MESSAGE + json.dumps({"role": role, "content": content}))
