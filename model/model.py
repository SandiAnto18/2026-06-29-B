import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
       self._idMap = {}
       self._graph=nx.Graph()

    def buildGraph(self):
        # COSTRUIAMO I NODI
        self._graph.clear()
        self._album = DAO.getAllAlbumByTracks()
        # STO COSTRUENDO UN DIZIONARIO CON CHIAVE ALBUMID E VALORE carattereische dell'aLBUMid ,OSSIA OGGETTO ALBUM completo.
        # così con l' idnumerico recupero l'oggetto artist corrispondente altrimenti mi da errore
        for a in self._album:
            self._idMap[a.AlbumID] = a
        self._graph.add_nodes_from(self._album)

        self._get2AlbumsByGenere=DAO.get2AlbumsByGenere() # IN INPUT NON HO NIENTE
        for a,b in self._get2AlbumsByGenere():
            self._graph.add_edges_from(self._get2AlbumsByGenere())

    def getNodes(self):
        return len(self._graph.nodes())
    def getEdges(self):
        return len(self._graph.edges())


