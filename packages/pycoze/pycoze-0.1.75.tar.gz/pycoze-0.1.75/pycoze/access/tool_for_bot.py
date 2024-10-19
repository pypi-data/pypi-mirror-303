import sys
import os
import importlib
from langchain.agents import tool as _tool
import types
import langchain_core


def change_directory_and_path(module_path):
    """Change the current working directory and sys.path."""
    sys.path.insert(0, module_path)
    os.chdir(module_path)


def restore_directory_and_path(module_path, old_path):
    """Restore the original working directory and sys.path."""
    sys.path.remove(module_path)
    os.chdir(old_path)


def wrapped_tool(tool, module_path):
    """Wrap the tool function to include additional logging and path management."""
    original_tool_function = tool.func

    def _wrapped_tool(*args, **kwargs):
        print(f"调用了{tool.name}")
        old_path = os.getcwd()
        try:
            change_directory_and_path(module_path)
            result = original_tool_function(*args, **kwargs)
        finally:
            restore_directory_and_path(module_path, old_path)
        print(f"{tool.name}调用完毕,结果为:", result)
        return result

    return _wrapped_tool


def import_tools(tool_id):
    """Import tools from a specified tool_id."""
    tool_base_path = "../../tool"
    old_path = os.getcwd()
    module_path = os.path.join(tool_base_path, tool_id)
    module_path = os.path.normpath(os.path.abspath(module_path))

    if not os.path.exists(module_path):
        print(f"Tool {tool_id} not found")
        return []

    # Save the current sys.modules state
    original_modules = sys.modules.copy()

    try:
        change_directory_and_path(module_path)
        module = importlib.import_module("tool")
        export_tools = getattr(module, "export_tools")
        valid_tools = []
        for tool in export_tools:
            assert isinstance(tool, langchain_core.tools.StructuredTool) or isinstance(
                tool, types.FunctionType
            ), f"Tool is not a StructuredTool or function: {tool}"
            if isinstance(tool, types.FunctionType) and not isinstance(
                tool, langchain_core.tools.StructuredTool
            ):
                valid_tools.append(_tool(tool))
        export_tools = valid_tools

    except Exception as e:
        print(f"Error loading tool {tool_id}: {e}")
        restore_directory_and_path(module_path, old_path)
        return []

    # Unload modules and restore sys.modules state
    importlib.invalidate_caches()
    for key in list(sys.modules.keys()):
        if key not in original_modules:
            del sys.modules[key]

    restore_directory_and_path(module_path, old_path)

    for tool in export_tools:
        tool.func = wrapped_tool(tool, module_path)

    return export_tools
