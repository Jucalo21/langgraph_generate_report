from agent.agent import run_graph

theme = input("Tema de la investigación: ")
number_queries = input("Número de consultas: ")

run_graph(
    theme=theme,
    number_queries=int(number_queries),
)
