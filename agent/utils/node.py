from agent.utils.tools import definir_llm, tavily_search
from docx import Document as DocxDocument
from dotenv import load_dotenv
from agent.utils.state import InformationResearcher, Document, Query
import os, json

load_dotenv()


def create_queries(state: InformationResearcher):
    client = definir_llm()

    prompt = f"""
    Vas a crear un numero de consultas que ayuden a investigar más a fondo el tema dado.
    Solo vas a entregar las consultas ni más ni menos.

    Tematica:
    <theme>{state['theme']}</theme>
    Numero de consultas:
    <number_queries>{state['number_queries']}</number_queries>
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Query,
        },
    )

    parsed = json.loads(response.text)
    state["queries"] = Query(queries=parsed.get("queries", []))

    return state


def investigate_queries(state: InformationResearcher):
    query_list = state["queries"].queries

    info_acumulada = ""
    for query in query_list:
        result = tavily_search(query)

        info_acumulada += result.get("summary", "") + "\n"
    state["info_documento"] = info_acumulada.strip()

    print(
        f"""
    La información acumulada es:
    {state['info_documento']}
    """
    )
    return state


def create_report(state: InformationResearcher) -> Document:

    prompt = f"""
    Te encargaras de crear un reportebien estructurado teniendo en cuenta la información acumulada de la tematica de la investigación 
    y las partes en las que se divide dicho reporte.

    Tematica:
    <theme>{state['theme']}</theme>
    Información acumulada:
    <info_documento>{state['info_documento']}</info_documento>
    
    Partes en las que se divide el reporte:
    1. Titulo
    2. Introducción
    3. Cuerpo
    4. Conclusion
    """

    client = definir_llm()

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Document,
        },
    )

    parsed = json.loads(response.text)

    return Document(**parsed)


def create_document(state: Document) -> None:

    # Crear un nuevo documento de word
    doc = DocxDocument()

    # Agregar el titulo
    doc.add_heading(state.title, level=1)

    # Agregar la introduccion
    doc.add_paragraph(state.introduction)

    # Agregar el cuerpo
    doc.add_paragraph(state.body)

    # Agregar la conclusion
    doc.add_paragraph(state.conclusion)

    # Guardar el documento
    doc.save("output/reporte.docx")
    print("Documento Generado")
    return state
