from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._list_objects = []
        self._get_objects()

        self._dict_objects = {}
        for obj in self._list_objects:
            self._dict_objects[obj.object_id] = obj

        self._graph = nx.Graph()

    def _get_objects(self):
        self._list_objects = DAO.readObjects()
        #print(self._list_objects)

    def buildGraph(self):
        # creazione dei nodi
        self._graph.add_nodes_from(self._list_objects)

        connessioni = DAO.readConnessioni(self._dict_objects)
        for c in connessioni:
            self._graph.add_edge(c.o1, c.o2, peso = c.peso)