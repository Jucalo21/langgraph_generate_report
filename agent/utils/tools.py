from dotenv import load_dotenv
from tavily import TavilyClient
from google import genai
import os

load_dotenv()


def tavily_search(query: str) -> dict:
    try:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("TAVILY_API_KEY no está configurada")

        client = TavilyClient(api_key)
        response = client.search(
            query=query,
            max_results=10,
            include_answer="advanced",
            include_raw_content=True,
        )

        return response

    except Exception as e:
        print(f"Error al buscar sobre la consulta {query}: {str(e)}")
        return {}


def definir_llm():

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    return client
