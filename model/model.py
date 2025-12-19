from networkx.classes import neighbors

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

        self.selected_object = None

        self.soluzione_migliore = None
        self.maxPeso = None

    def _get_objects(self):
        self._list_objects = DAO.readObjects()
        #print(self._list_objects)

    def buildGraph(self):
        # creazione dei nodi
        self._graph.add_nodes_from(self._list_objects)

        connessioni = DAO.readConnessioni(self._dict_objects)
        for c in connessioni:
            self._graph.add_edge(c.o1, c.o2, peso = c.peso)

    def calcolaConnessa(self, obj_id):
        self.selected_object = self._dict_objects[obj_id]

        tree = nx.dfs_tree(self._graph, self.selected_object)
        num_conn = tree.nodes
        return len(num_conn)

    def cercaOggetti(self, lunghezza):

        self.soluzione_migliore = []
        self.maxPeso = 0
        partenza = self.selected_object

        self._ricorsione([partenza], [partenza], lunghezza)

        return self.soluzione_migliore, self.maxPeso

    def _ricorsione(self, parziale, visitati, lunghezza):
        if len(parziale) == lunghezza:
            peso = self.calcolaPeso(parziale)
            if peso > self.maxPeso :
                self.maxPeso = peso
                self.soluzione_migliore = parziale

        for v in neighbors(self._graph, parziale[-1]):
            if v not in visitati and v.classification == parziale[-1].classification:
                visitati.append(v)
                parziale.append(v)
                self._ricorsione(parziale, visitati, lunghezza)
                visitati.pop()
                parziale.pop()

    def calcolaPeso(self, parziale):
        peso = 0
        for i in range(len(parziale)-1):
            v = parziale[i]
            u = parziale[i+1]
            peso += self._graph[v][u]['peso']
        return peso