import asyncio

from mcp1.client import MCPClient


async def test():

    client = MCPClient()

    try:

        session = await client.connect(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-github"
            ],
        )

        print("Connected Successfully")

    finally:

        await client.disconnect()


asyncio.run(test())