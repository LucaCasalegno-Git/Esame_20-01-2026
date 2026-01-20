from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:


    @staticmethod
    def get_artists_album(album):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select a.id, a.name, count(*) as num_album
                from artist a, album al
                where a.id = al.artist_id 
                group by a.id, a.name 
                having num_album  >= %s  """
        cursor.execute(query, (album,))
        for row in cursor:
            artista = Artist(id=row['id'], name=row['name'], n_album=row['num_album'])
            result.append(artista)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni(album):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """query...
                 """
        cursor.execute(query)
        for row in cursor:

            result.append(artista)
        cursor.close()
        conn.close()
        return result


