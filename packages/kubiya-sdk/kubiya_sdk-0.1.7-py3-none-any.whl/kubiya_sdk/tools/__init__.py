import os

from .models import (
    Tool,
    Source,
    Arg,
    ToolOutput,
    FileSpec,
    Volume,
    ServiceSpec,
    GitRepoSpec,
    OpenAPISpec,
)
from .registry import tool_registry
from .function_tool import FunctionTool
from .tool_manager_bridge import ToolManagerBridge
from .tool_func_wrapper import function_tool

__all__ = [
    "Tool",
    "Source",
    "Arg",
    "ToolOutput",
    "tool_registry",
    "FunctionTool",
    "ToolManagerBridge",
    "FileSpec",
    "Volume",
    "ServiceSpec",
    "GitRepoSpec",
    "OpenAPISpec",
    "function_tool",
]

if not os.getenv("TOOL_MANAGER_URL"):
    print(
        "TOOL_MANAGER_URL environment variable not set. Defaulting to http://localhost:8000"
    )
    os.environ["TOOL_MANAGER_URL"] = "http://localhost:8000"
