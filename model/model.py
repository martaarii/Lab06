from database import DAO, product_DAO, ratail_DAO


class Model:
    def __init__(self):
        self.sales = DAO.Sale_DAO()
        self.product = product_DAO.product_DAO()
        self.retailer = ratail_DAO.Retail_DAO()

    def get_dates(self):
        return self.sales.get_dates()
    def get_brands(self):
        return self.product.get_brands()
    def get_retailers(self):
        return self.retailer.get_Retails()
    def vendite_migliori(self, anno, venditore, brand):
        return self.sales.vendite_migliori(anno, venditore, brand)
    def vendite_analisi(self,anno, venditore, brand):
        vendite = self.sales.vendite_cercate(anno, venditore, brand)
        return vendite
