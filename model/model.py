import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):

       self._graph=nx.Graph()

    def buildGraph(self):
        self._graph.clear()
        #RESITUISCO TUTTI GLI ALBUM
        albums= DAO.getAllAlbums()
        #RIEMPO ATTRIBUTO TRACKS PER OGNI ALBUM
        for album in albums:
            album.Tracks=DAO.getTracksByAlbum(album.AlbumId)

        self._graph.add_nodes_from(albums)
        #COSTRUISCO MAPPA PER CONVERTIRE ID DEGLI ALBUM IN OGGETTI ALBUM
        ArchiMap = {}
        for album in albums:
            ArchiMap[album.AlbumId]=album

        archi=DAO.getAlbum1Album2byGenre()
        for a1,a2 in archi:
            album1=ArchiMap[a1]
            album2=ArchiMap[a2]
            self._graph.add_edge(album1,album2) #sol
            #TypeError: Graph.add_edges_from() takes 2 positional arguments but 3 were given






    def getNodes(self):
        return len(self._graph.nodes())
    def getEdges(self):
        return len(self._graph.edges())

    def TotCompConnesse(self):

        comp= list(nx.connected_components(self._graph))
        return comp

    def getLargestComp(self, comp):
        largest =(max(comp, key=len)) # scegli il max (confronta le componenti in base alla loro lunghezza)
        largestOrdinata= sorted(largest, key=lambda x:x.Title) #ordino oggetti album in ordine alfabetico
        return largestOrdinata
