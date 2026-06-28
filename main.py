from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import search_tool, wiki_tool, save_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

agent = create_agent(
    model=llm,
    tools=[
        search_tool,
        wiki_tool,
        save_tool
    ],
    system_prompt="""
You are a research scientist.

Use the available tools whenever necessary.
Use the search tool to find information on the web.
Use the wikipedia tool for factual/encyclopedic topics.
Use the save tool to save your findings to a file.

Always return:
- topic
- summary
- sources
- tools_used
""",
    response_format=ResearchResponse,
)

query = input("Enter your query: ")

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
)

print(response["structured_response"])