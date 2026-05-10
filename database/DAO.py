from database.DB_connect import DBConnect
from model.airport import Airport


class DAO():

    @staticmethod
    def getAllAirports_num(numero_min_comp):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """with aerop_numero_comp as(
                    select f.ORIGIN_AIRPORT_ID as ido, count(f.AIRLINE_ID ) as num_comp
                    from flights f 
                    group by f.ORIGIN_AIRPORT_ID )
                    select a.*
                    from airports a, aerop_numero_comp anc
                    where a.ID =anc.ido and anc.num_comp >= %s
                    """

        cursor.execute(query, (numero_min_comp, ))

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select least(f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID )as ido, greatest(f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID) as idd, count(*) as peso
                    from flights f
                    group by LEAST(f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID ), greatest(f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID )
                        """

        cursor.execute(query)

        for row in cursor:
            result.append((row["ido"], row["idd"], row["peso"]))

        cursor.close()
        conn.close()
        return result