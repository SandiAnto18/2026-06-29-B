from dataclasses import dataclass

from model import Track


@dataclass
class Album:
    AlbumId: int
    Title: str
    ArtistId:int
    Tracks:list[Track]=None #può	risultare	conveniente
#aggiungere	alla	relativa	classe	un	attributo
#aggiuntivo	che	memorizzi	la	lista	di	tutti	i
#brani	appartenenti	a	quell'album.
#CREO CLASSE TRACK
#hash permette di identificare al grafo di identificare correttamente
    def __hash__(self):
        return hash(self.AlbumId)

    #per tenere traccia dell'album A e numero di brani xA
    def __str__(self):
        return f"{self.Title}"