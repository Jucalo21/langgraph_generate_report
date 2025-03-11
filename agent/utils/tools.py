from dotenv import load_dotenv
from tavily import TavilyClient
from google import genai
import os

load_dotenv()


def tavily_search(query: str) -> dict:

    api_key = os.getenv("TAVILY_API_KEY")
    client = TavilyClient(api_key)

    response = client.search(query=query)

    print(response)


def definir_llm():

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    return client
