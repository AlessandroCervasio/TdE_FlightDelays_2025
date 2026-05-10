import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_compagnieMinimo= None
        self.btn_analizzaAeroporti = None
        self.btn_testConnessione = None
        self._dd_aeroportoPartenza=None
        self._dd_aeroportoDest=None
        self.txt_result = None



    def load_interface(self):
        # title
        self._title = ft.Text("Flight Delays", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_compagnieMinimo = ft.TextField(
            label="# compagnie minimo",
            width=200,
        )
        self._dd_aeroportoPartenza=ft.Dropdown(expand=True, label="Aeroporto di partenza", disabled=True)
        self._dd_aeroportoDest=ft.Dropdown(expand=True, label="Aeroporto destinazione", disabled=True)

        # button for the "hello" reply
        self.btn_analizzaAeroporti = ft.ElevatedButton(text="Analizza Aeroporti", on_click=self._controller.handleAnalizzaAeroporti)
        self.btn_testConnessione = ft.ElevatedButton(text="Test Connessione", on_click=self._controller.handleTestConnessione)

        row1 = ft.Row([self.txt_compagnieMinimo, self.btn_analizzaAeroporti],
                       width=400)
        self._page.controls.append(row1)
        row2 = ft.Row([self._dd_aeroportoPartenza],
                      width=400)
        self._page.controls.append(row2)
        row3 = ft.Row([self._dd_aeroportoDest],
                      width=400)
        self._page.controls.append(row3)
        row4 = ft.Row([self.btn_testConnessione],
                      width=200)
        self._page.controls.append(row4)


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
