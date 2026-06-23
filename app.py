# # import asyncio

# # from config.constants import EXIT_COMMANDS

# # from llm.model import LLMFactory

# # from mcp1.client import MCPClient
# # from mcp1.loader import MCPToolLoader

# # from agent.github_agent import GitHubAgent
# # from config.settings import Settings

# # async def main():

# #     client = MCPClient()

# #     try:

# #         session = await client.connect(
# #             command="npx",
# #             args=[
# #                 "-y",
# #                 "@modelcontextprotocol/server-github"
# #             ],
# #             env={
# #                 "GITHUB_TOKEN": Settings.GITHUB_TOKEN
# #         }
# #         )

# #         tools = await MCPToolLoader.load(
# #             session
# #         )

# #         llm = LLMFactory.create()

# #         github_agent = GitHubAgent(
# #             llm=llm,
# #             tools=tools
# #         )

# #         print("\nGitHub MCP Agent Ready\n")

# #         while True:

# #             query = input("You > ")

# #             if query.lower() in EXIT_COMMANDS:
# #                 break

# #             result = github_agent.invoke(
# #                 query
# #             )

# #             print(
# #                 "\nAssistant >",
# #                 result["output"],
# #                 "\n"
# #             )

# #     finally:

# #         await client.disconnect()


# # if __name__ == "__main__":

# #     asyncio.run(main())
# import asyncio
# # Run 'pip install aioconsole' if you don't have it installed
# import aioconsole 

# from config.constants import EXIT_COMMANDS
# from llm.model import LLMFactory
# from mcp1.client import MCPClient
# from mcp1.loader import MCPToolLoader
# from agent.github_agent import GitHubAgent
# from config.settings import Settings
# # Settings.GITHUB_TOKEN
# async def main():
#     client = MCPClient()

#     try:
#         # The ** unpacks the dictionary keys directly into positional arguments
#         session = await client.connect(**{
#             "command": "cmd.exe",
#             "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-github"],
#             "env": {
#                 "GITHUB_PERSONAL_ACCESS_TOKEN":Settings.GITHUB_TOKEN 
#             }
#         })


#         tools = await MCPToolLoader.load(session)
#         llm = LLMFactory.create()

#         github_agent = GitHubAgent(
#             llm=llm,
#             tools=tools
#         )

#         print("\nGitHub MCP Agent Ready\n")

#         while True:
#             query = await aioconsole.ainput("You > ")

#             if query.strip().lower() in EXIT_COMMANDS:
#                 break

#             result = await github_agent.invoke(query)

#             print(
#                 "\nAssistant >",
#                 result.get("output", "No output returned."),
#                 "\n"
#             )

#     except Exception as e:
#         print(f"\nAn error occurred during execution: {e}\n")

#     finally:
#         await client.disconnect()


# if __name__ == "__main__":
#     asyncio.run(main())
import pprint
import asyncio
import os  # <-- Step 1: Import the built-in os module
import aioconsole 
import traceback
from config.constants import EXIT_COMMANDS
from llm.model import LLMFactory
from mcp1.client import MCPClient
from mcp1.loader import MCPToolLoader
from agent.github_agent import GitHubAgent
from config.settings import Settings

async def main():
    client = MCPClient()

    try:
        # Step 2: Build a robust environment dictionary that inherits your system's PATH
        server_env = {
            **os.environ,
            "GITHUB_TOKEN": Settings.GITHUB_TOKEN,
            "GITHUB_PERSONAL_ACCESS_TOKEN": Settings.GITHUB_TOKEN,
        }

        # Step 3: Connect using the Windows fallback but with full environment mapping
        session = await client.connect(**{
            "command": "npx.cmd",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": server_env
        })
        print("Connected successfully")
        
        tools = await MCPToolLoader.load(session)
        llm = LLMFactory.create()
        selected_tools = [
            t for t in tools
            if t.name in [
                "search_repositories",
                "create_repository",
                "get_file_contents",
                "search_code",
                "list_commits",
            ]
        ]
        github_agent = GitHubAgent(
            llm=llm,
            tools=selected_tools
        )

        print("\nGitHub MCP Agent Ready\n")

        while True:
            query = await aioconsole.ainput("You > ")

            if query.strip().lower() in EXIT_COMMANDS:
                break

            result = await github_agent.invoke(query)


            print("\nRAW RESULT:")
            pprint.pp(result)
            print()

    # except Exception as e:
    #     print(f"\nAn error occurred during execution: {e}\n")

    except Exception:
            print("\nFULL ERROR:\n")
            traceback.print_exc()

    finally:
            await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
