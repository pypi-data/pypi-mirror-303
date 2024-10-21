import sys
import json


def read_arg(param, is_path=False, posix=True):
    while param.startswith("-"):
        param = param[1:]
    args = sys.argv[1:]
    for i in range(len(args)):
        if args[i] == "-" + param or args[i] == "--" + param:
            value = args[i + 1]
            break
    if is_path and value:
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        if posix:
            value = value.replace("\\", "/")

    return value


def read_params_file():
    params_file = read_arg("params_file", True)
    params = None
    try:
        with open(params_file, "r", encoding="utf-8") as f:
            params = json.load(f)
    except Exception as e:
        print(e)
    return params
