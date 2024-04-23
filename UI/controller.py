import flet as ft
from model import model

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def riempi_anni(self):
        date = self._model.get_dates()
        self._view.dd_anno.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for data in date:
            self._view.dd_anno.options.append(ft.dropdown.Option(data))
        self._view.update_page()

    def riempi_brand(self):
        brands = self._model.get_brands()
        self._view.dd_brand.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand))
        self._view.update_page()

    def riempi_retailer(self):
        retailers = self._model.get_retailers()
        self._view.dd_retailer.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(retailer))
        self._view.update_page()

    def handle_top_vendite(self, e):
        self._view.txt_result.clean()
        venditore = self._view.dd_retailer.value
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        if venditore == "Nessun filtro":
            venditore = None
        if anno == "Nessun filtro":
            anno = None
        if brand == "Nessun filtro":
            brand = None

        vendite_top = self._model.vendite_migliori(anno, venditore, brand)
        for element in vendite_top:
            self._view.txt_result.controls.append(ft.Text(f"Anno: {element.date}, Ricavo:"
                                                          f"{element.quantity*element.unit_sale_price},"
                                                          f"Rivenditore:{element.retailer_code}, "
                                                          f"Prodotto:{element.product_number}"))
        self._view.update_page()
    def handle_analisi_vendite(self, e):
        self._view.txt_result.clean()
        venditore = self._view.dd_retailer.value
        anno = self._view.dd_anno.value
        brand = self._view.dd_brand.value
        if venditore == "Nessun filtro":
            venditore = None
        if anno == "Nessun filtro":
            anno = None
        if brand == "Nessun filtro":
            brand = None

        vendite = self._model.vendite_analisi(anno, venditore, brand)
        giro_affari = 0
        numero_vendite = 0
        venditori = []
        for vendita in vendite:
            giro_affari += (vendita.quantity * vendita.unit_sale_price)
            numero_vendite += 1
            if not venditori.__contains__(vendita.retailer_code):
                venditori.append(vendita.retailer_code)

        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari : {giro_affari}\n"
                                                      f"Numero di vendite: {numero_vendite}\n"
                                                      f"Numero di venditori coinvolti: {len(venditori)}\n"))

        self._view.update_page()

