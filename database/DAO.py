from database.DB_connect import DBConnect
from model.Album import Album
from model.Track import Track


class DAO():

    @staticmethod
    def getAllAlbums():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)

        query = """
                select distinct a.*
from album a, track t
where t.AlbumId =a.AlbumId 
                """

        cursor.execute(query)

        for row in cursor:
            results.append(Album(**row))

        cursor.close()
        conn.close()

        return results

    # OUTPUT album preso come oggetto: albumid|title|artistid

    @staticmethod
    def getTracksByAlbum(AlbumId):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)

        query = """select t.*
from track t
where t.AlbumId =%s
                
                """

        cursor.execute(query,(AlbumId,))

        for row in cursor:
            results.append(Track(**row))

        cursor.close()
        conn.close()

        return results

#output Trackid| Name| Albumid|.. |Unit pRICE


    @staticmethod
    def getAlbum1Album2byGenre():#non servono i nodi in input perchè il grafo ha già tutti gli album come nodi e sono stati già costruiti.
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)

        query = """select distinct a.AlbumId as album1 ,a2.AlbumId as album2
from album a, track t, album a2,track t2
where a.AlbumId =t.AlbumId 
and a2.AlbumId =t2.AlbumId 
and t.GenreId =t2.GenreId
and a.AlbumId < a2.AlbumId 

                """

        cursor.execute(query)

        for row in cursor:
            results.append((row['album1'], row['album2']))

        cursor.close()
        conn.close()

        return results













