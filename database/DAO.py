from database.DB_connect import DBConnect
from model import sales


class Sale_DAO():
    def __init__(self):
        pass
    def get_dates(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connesione")
            return
        else:
            query = """ SELECT distinct YEAR(date) as Year 
                        FROM go_daily_sales;
                    """
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor:
                result.append(row['Year'])
            cursor.close()
            cnx.close()

            return result

    def vendite_migliori(self, anno, venditore, brand):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connesione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                        SELECT *
                        FROM go_daily_sales gds 
                        WHERE (Retailer_code= (select Retailer_code from go_retailers gr 
                        where retailer_name = %s) OR %s IS null)
                        and (year (`Date`)= %s or %s is null)
                        and (Product_number in (select Product_number from go_products gp  
                        where product_brand = %s) or %s is null)
                        order by (Quantity*Unit_sale_price) desc 
                        LIMIT 5;
                    """
            cursor.execute(query, (venditore,venditore,anno,anno,brand,brand))
            print("query eseguita")
            for row in cursor:
                result.append(sales.Sale(row['Retailer_code'], row['Product_number'], row['Order_method_code'],
                                         row['Date'], row['Quantity'], row['Unit_price'], row['Unit_sale_price']))
                print("riga")
            cursor.close()
            cnx.close()

        return result

    def vendite_cercate(self, anno, venditore, brand):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connesione")
            return
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                                SELECT *
                                FROM go_daily_sales gds 
                                WHERE (Retailer_code= (select Retailer_code from go_retailers gr 
                                where retailer_name = %s) OR %s IS null)
                                and (year (`Date`)= %s or %s is null)
                                and (Product_number in (select Product_number from go_products gp  
                                where product_brand = %s) or %s is null);
                            """
            cursor.execute(query, (venditore, venditore, anno, anno, brand, brand))
            for row in cursor:
                result.append(sales.Sale(row['Retailer_code'], row['Product_number'], row['Order_method_code'],
                                         row['Date'], row['Quantity'], row['Unit_price'], row['Unit_sale_price']))

            cursor.close()
            cnx.close()

        return result
