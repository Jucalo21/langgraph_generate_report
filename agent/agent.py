from langgraph.graph import StateGraph, END, START
from agent.utils.state import ResearchState, InformationResearcher, Document, Query
from agent.utils.node import (
    create_queries,
    investigate_queries,
    create_report,
    create_document,
)


def run_graph():
    initial_state = ResearchState(
        researcher=InformationResearcher(
            theme="""
            Celulares de gama media-alta, los cuales tengan una buena relación calidad-precio.
            """,
            queries=Query(queries=[]),
            number_queries=5,
            info_documento="",
        ),
        document=Document(
            title="",
            introduction="",
            body="",
            conclusion="",
        ),
    )

    graph_builder = StateGraph(ResearchState)
    graph_builder.add_node("create_queries", create_queries)
    graph_builder.add_node("investigate_queries", investigate_queries)
    graph_builder.add_node("create_report", create_report)
    graph_builder.add_node("create_document", create_document)

    graph_builder.add_edge(START, "create_queries")
    graph_builder.add_edge("create_queries", "investigate_queries")
    graph_builder.add_edge("investigate_queries", "create_report")
    graph_builder.add_edge("create_report", "create_document")
    graph_builder.add_edge("create_document", END)

    graph = graph_builder.compile()
    graph.invoke(initial_state)
