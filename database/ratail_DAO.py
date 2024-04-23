import database.DB_connect
from database.DB_connect import DBConnect

class Retail_DAO:
    def get_Retails(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connesione")
            return
        else:
            query = """ SELECT distinct Retailer_name  
                        from go_retailers gr;
                    """
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor:
                result.append(row["Retailer_name"])
            cursor.close()
            cnx.close()

            return result