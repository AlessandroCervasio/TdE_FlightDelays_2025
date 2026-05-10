from model.model import Model

mdl=Model()
grafo=mdl.buildGraph(400)
print(f"Il grafo ha {mdl.get_num_nodes()} nodi e {mdl.get_num_edges()} archi")
