from langchain_mcp_adapters.tools import load_mcp_tools


class MCPToolLoader:

    @staticmethod
    async def load(session):

        tools = await load_mcp_tools(session)
        for tool in tools:
            print(tool.name)
        return tools