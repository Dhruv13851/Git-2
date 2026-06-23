from langchain_groq import ChatGroq

from config.settings import Settings


class LLMFactory:

    @staticmethod
    def create():

        return ChatGroq(
            api_key=Settings.GROQ_API_KEY,
            model=Settings.GROQ_MODEL,
            temperature=0
        )