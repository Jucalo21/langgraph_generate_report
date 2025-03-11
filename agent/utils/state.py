from pydantic import BaseModel, Field
from typing import TypedDict, List


class Query(BaseModel):
    queries: List[str] = Field(
        description="Lista de consultas generadas mediante un llamado a LLM"
    )


class InformationResearcher(BaseModel):
    theme: str = Field(
        description="Tematica de la investigación",
    )
    queries: Query = Field(
        description="Consultas generadas para la investigacion",
    )
    number_queries: int = Field(
        description="Numero de consultas ha generar para la investigacion",
    )
    info_documento: str = Field(
        description="Información de las consultas generadas mediante tavily ",
    )


class Document(BaseModel):
    title: str = Field(
        description="Titulo del documento, teniendo en cuenta la tematica de la investigación"
    )
    introduction: str = Field(
        description="Introduccion del documento, teniendo en cuenta la tematica de la investigación"
    )
    body: str = Field(
        description="Cuerpo del documento, teniendo en cuenta la tematica de la investigación."
    )
    conclusion: str = Field(
        description="Conclusion del documento, teniendo en cuenta la tematica de la investigación."
    )
