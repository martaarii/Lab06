import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_top_vendite = None
        self.btn_analisi_vendite = None
        self.txt_name = None
        self.btn_hello = None
        self.lst_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        # 3 menu a tendina con anno, brand, rivenditore

        self.dd_anno = ft.Dropdown(
            label="Anno", options=[], width=200,
            hint_text="Selezionare l'anno di interesse")
        self.controller.riempi_anni()

        self.dd_retailer = ft.Dropdown(
            label="Rivenditore", options=[], width=200,
            hint_text="Selezionare il rivenditore")
        self.controller.riempi_retailer()

        self.dd_brand = ft.Dropdown(
            label="Brand", options=[], width=200,
            hint_text="Selezionare il brand")
        self.controller.riempi_brand()

        row1 = ft.Row([self.dd_anno, self.dd_brand, self.dd_retailer],
                      alignment=ft.MainAxisAlignment.CENTER)

        # Row 2
        # 2 bottoni per top vendite e analizzare vendite

        self.btn_top_vendite= ft.ElevatedButton(text="Top vendite",
                                                on_click=self._controller.handle_top_vendite)
        self.btn_analisi_vendite = ft.ElevatedButton(text="Analizza vendite",
                                                     on_click=self._controller.handle_analisi_vendite)
        row2 = ft.Row([self.btn_top_vendite, self.btn_analisi_vendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
