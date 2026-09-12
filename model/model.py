import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
       self._idMap = {}
       self._graph=nx.Graph()

    def buildGraph(self):
       #LE GGE TUTTI GLI ALBUM DAL DATABASE
        albums= DAO.getAllAlbumByTracks()
    #PRENDI UN OGGETTO ALLA VOLTA DI ALBUMS E LO POPOLI CON LE SUE TRACCIA
        for a in albums:
            DAO.getTracksForAlbum(a) #prendi tutte le sue tracce e aggiungile ad album a
        self._graph.add_nodes_from(albums) #poi li aggiungi tutti come nodi

    #DEVO CHIAMARE IL METODO _SHARE GENRE PER COSTRUIRE GLI ARCHI
    #è importante distinguere tra quando scrivi i metodi
    #e quando Python li esegue. _shareGenre può essere definito sotto,
    #ma viene eseguito solo quando viene chiamato da build graph

    #DOPPIO CICLO NEI NODI PER VEDERE SE DUE ALBUM HANNO UN GENERE IN COMUNE
    #IL DOPPIO CICLO NON CREA DCIRETTAMENTE GLI ARCHI MA PREPARA 2 NODI ALLA VOLTA
    #SE è VERA ALLORA ADD EDGE CREA EFFETTIVAMENTE L'ARCO


        for i,album1 in enumerate(albums):#scorre la lista albums e restituisce la posizione i e il suo ogg.album
        #album1 [i=0 a1,i=1 a2, i=2 a3]
        #il 2do for prende solo gli album successivi alla posizone i e crea gli archi tra le coppie, senza duplicati
          for album2 in albums[i+1:]:# album2 scorre gli album che vengono dopo quell'indice
              #così non paragoni un album con se stesso e non ripeti coppie al contrario.
            if self._shareGenre(album1,album2): #se _shareGenre diche che condividono un genere
                self._graph.add_edge(album1,album2) #allora aggiungi arco


    #Esiste	un arco tra due album distinti A1eA2 se i due album hanno almeno un genere in comune
    def _shareGenre(self,album1,album2):
    # SE MANCA LA LISTA DELLE TRACCE NON POSSIAMO CONTROLLARE  I GENERI
        if album1.Tracks is None or album2.Tracks is None:
            return False

    #album1:prendo i suoi tracks, da ogni brano prendo il genreid e li metto tutti assieme nella variabile genre1)
    #set raggruppa eliminando i duplicati
    #STO COSTRUENDO L'INSIEME(diverso da lista/mappa) DEI GENERI DIVERSI PRESENTI TRA LE TRACCE DI ALBUM 1
        genre1= set(track.GenreId for track in album1.Tracks if track.GenreId is not None)
    # GENERI PRESENTI NELL'ALBUM2
        genre2= set(track.GenreId for track in album2.Tracks if track.GenreId is not None)

        # costruiti i 2 elenchi di generi verifico l'intersezione
        return len(genre1.intersection(genre2))>0



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
