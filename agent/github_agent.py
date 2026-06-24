# from langchain.agents import AgentExecutor
# from langchain.agents import create_tool_calling_agent

# from langchain_core.prompts import ChatPromptTemplate

# from prompts.system_prompt import SYSTEM_PROMPT


# class GitHubAgent:

#     def __init__(
#         self,
#         llm,
#         tools
#     ):

#         self.llm = llm
#         self.tools = tools

#         self.agent_executor = self._build()

#     def _build(self):

#         prompt = ChatPromptTemplate.from_messages(
#             [
#                 ("system", SYSTEM_PROMPT),
#                 ("human", "{input}"),
#                 ("placeholder", "{agent_scratchpad}")
#             ]
#         )

#         agent = create_tool_calling_agent(
#             llm=self.llm,
#             tools=self.tools,
#             prompt=prompt
#         )

#         return AgentExecutor(
#             agent=agent,
#             tools=self.tools,
#             verbose=True
#         )

#     def invoke(
#         self,
#         query: str
#     ):

#         return self.agent_executor.invoke(
#             {
#                 "input": query
#             }
#         )
from langchain.agents import create_agent
from prompts.system_prompt import SYSTEM_PROMPT

class GitHubAgent:

    def __init__(self, llm, tools):
        self.agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt=SYSTEM_PROMPT,
            debug=True
        )

    async def invoke(self, query: str):

        result = await self.agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }
        )

        return result