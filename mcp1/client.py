from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters


class MCPClient:

    def __init__(self):

        self.exit_stack = AsyncExitStack()

        self.session = None

    async def connect(
        self,
        command: str,
        args: list[str],
        env: dict | None = None
    ):

        server_params = StdioServerParameters(
            command=command,
            args=args,
            env=env
        )

        stdio_transport = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )

        read_stream, write_stream = stdio_transport

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(
                read_stream,
                write_stream
            )
        )

        await self.session.initialize()

        return self.session

    async def disconnect(self):

        await self.exit_stack.aclose()

