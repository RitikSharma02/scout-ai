from datetime import datetime

from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool


@tool
def search(query: str) -> str:
    """Search the web for information using DuckDuckGo."""
    ddg = DuckDuckGoSearchRun()
    return ddg.run(query)


@tool
def wiki(query: str) -> str:
    """Look up factual and encyclopedic information on Wikipedia."""
    api_wrapper = WikipediaAPIWrapper(
        top_k_results=1,
        doc_content_chars_max=1000
    )
    wiki_runner = WikipediaQueryRun(api_wrapper=api_wrapper)
    return wiki_runner.run(query)


@tool
def save_to_file(data: str, filename: str = "research_output.txt") -> str:
    """Save research output text to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"----- {timestamp} -----\n")
        f.write(data)
        f.write("\n\n")

    return f"Saved to {filename}"


search_tool = search
wiki_tool = wiki
save_tool = save_to_file