from typing import Dict, Optional
from .models import Tool
from typing import List

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Dict[str, Tool]] = {}

    def register(self, source: str, tool: Tool):
        if source not in self.tools:
            self.tools[source] = {}
        self.tools[source][tool.name] = tool

    # Alias for register (for backwards compatibility)
    def register_tool(self, source: str, tool: Tool):
        self.register(source, tool)

    def get_tool(self, source: str, name: str) -> Optional[Tool]:
        return self.tools.get(source, {}).get(name)

    def list_tools(self, source: str) -> List[Tool]:
        return list(self.tools.get(source, {}).values())

tool_registry = ToolRegistry()