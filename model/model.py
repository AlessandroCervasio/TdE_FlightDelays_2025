import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph=None
        self._nodes=[]
        self._idMap={}

    def buildGraph(self, num_min_comp):
        self._graph=nx.Graph()
        self._nodes=DAO.getAllAirports_num(num_min_comp)
        for n in self._nodes:
            self._idMap[n.ID]=n
        self._graph.add_nodes_from(self._nodes)
        #print(len(self._idMap))
        lista=DAO.getAllEdges()
        for i in lista:
            if i[0] not in self._idMap or i[1] not in self._idMap:
                continue
            else:
                u= self._idMap[i[0]]
                v= self._idMap[i[1]]
                peso= int(i[2])
                self._graph.add_edge(u, v, weight=peso)


    def get_num_nodes(self):
        return len(self._graph.nodes)

    def get_num_edges(self):
        return len(self._graph.edges)

    def elementi_dd(self):
        #for i in self._graph.nodes:
            #print(type(i))
        return self._graph.nodes

    def ottieni_nodo(self, id):
        return self._idMap[int(id)]

    def has_path(self, source, target):
        return nx.has_path(self._graph, source, target)

    def percorso_minimo_djk(self, source, target):
        return nx.shortest_path(self._graph, source, target, weight="peso")