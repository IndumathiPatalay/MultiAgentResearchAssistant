from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os  
from langchain_tavily import TavilySearch
import rich
from bs4 import BeautifulSoup
#from readability import document
import trafilatura
import re


load_dotenv()

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic """
    #Intialize the TavilySearch tool
    search_tool = TavilySearch(max_results=5, topic="general",include_answer=True,tavily_api_key=os.getenv("TAVILY-API-KEY"), tavily_api_url=os.getenv("TAVILY-API-URL"))
    results = search_tool.run(query)
     
    out=[]
    for r in results['results']:
        out.append(f"Title: {r['title']}\nURL: {r['url']}\ncontent: {r['content']}\n")

    return "\n\n".join(out)

@tool
def extract_content_from_url(url: str) -> str:
    """Extract the main content from a given URL using trafilatura"""
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded is None:
            return "Failed to download content."
        result = trafilatura.extract(downloaded, include_comments=True, include_tables=True)
        return result if result else "No content extracted."
    except Exception as e:
        return f"Error extracting content: {str(e)}"

