from database.DB_connect import DBConnect
from model.Album import Album
from model.Track import Track


class DAO():

    @staticmethod
    def getAllAlbumByTracks():
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query= "select distinct a.* from album a,track t  where t.AlbumId=a.AlbumId order by a.Title"
        cursor.execute(query)

        for row in cursor:
            results.append(Album(row["AlbumId"],row["Title"],row["ArtistId"]))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getTracksForAlbum(a):
        # gli passo un album e lo popolo con i suoi tracks
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        #NON NECESSARIO CONDIZIONE DI WHERE PERCHè ABBIAMO GIà IN INPUT L'ALBUM ID CREATO NELLA QUERY DEI NODI
        #per avere  i rsultati in ordine alfabetico uso order by t.name
        query = "select t.* from track t,album a where t.AlbumId = a.AlbumId  and a.AlbumId = %s order by t.Name"
        cursor.execute(query, (a.AlbumId,)) #Prendi l'AlbumId dell'oggetto che hai ricevuto in input e lo usi per %s.
        for row in cursor:
            results.append(Track(**row))
            a.Tracks= results #"Ho trovato i Tracks e li metto direttamente dentro l'Album che mi hai passato:a.Tracks"
        a.Tracks=results

        cursor.close()
        conn.close()











