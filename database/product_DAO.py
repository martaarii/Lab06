from database.DB_connect import DBConnect
from model import product


class product_DAO():
    def __init__(self):
        pass

    def get_brands(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connesione")
            return
        else:
            query = """ SELECT distinct Product_brand 
                        from go_products gp ;
                    """
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor:
                result.append(row['Product_brand'])
            cursor.close()
            cnx.close()

            return result

    def get_products(self, brand):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connesione")
            return
        else:
            query = """ SELECT distinct Product_brand 
                                from go_products gp 
                                where product_brand = %s;
                            """
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (brand,))
            for row in cursor:
                result.append(product.Product(row['Product_number'], row['Product_line'], row['Product_type'],
                                         row['Product'], row['Product_brand'], row['Product_color'],
                                         row['Unit_cost'], row['Unit_price']))
            cursor.close()
            cnx.close()
        return result
