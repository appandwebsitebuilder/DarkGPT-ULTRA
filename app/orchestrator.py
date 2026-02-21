import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class DarkGPT_Orchestrator:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1"
        
        self.llm_claude = ChatOpenAI(model="anthropic/claude-3-sonnet", openai_api_key=self.api_key, openai_api_base=self.api_url)
        self.llm_gpt = ChatOpenAI(model="openai/gpt-4o-mini", openai_api_key=self.api_key, openai_api_base=self.api_url)

    def route_query(self, query: str, language: str):
        system_prompt = f"You are DarkGPT Pro, a Global AI for World Welfare. You MUST reply ONLY in {language}. Be highly helpful and kind."
        full_prompt = f"System: {system_prompt}\nUser: {query}"

        if "code" in query.lower() or "bug" in query.lower() or "error" in query.lower():
            response = self.llm_claude.invoke(full_prompt)
        else:
            response = self.llm_gpt.invoke(full_prompt)
            
        return response.content
