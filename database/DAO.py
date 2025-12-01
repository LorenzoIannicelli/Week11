from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.object import Object


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def readObjects():
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print('Connection failed.')
            return None
        else :
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM objects"""

            cursor.execute(query)

            for row in cursor:
                obj = Object(**row)
                result.append(obj)

            cursor.close()
            cnx.close()

            return result

    @staticmethod
    def readConnessioni(dict_objects):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print('Connection failed.')
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                    SELECT eo1.object_id AS o1, eo2.object_id AS o2, COUNT(*) as peso
                    FROM exhibition_objects eo1, exhibition_objects eo2
                    WHERE eo1.exhibition_id = eo2.exhibition_id 
                    AND eo1.object_id < eo2.object_id 
                    GROUP BY eo1.object_id, eo2.object_id
                    """

            cursor.execute(query)

            for row in cursor:
                o1 = dict_objects[row['o1']]
                o2 = dict_objects[row['o2']]
                peso = row['peso']
                result.append(Connessione(o1, o2, peso))

            cursor.close()
            cnx.close()

            return result