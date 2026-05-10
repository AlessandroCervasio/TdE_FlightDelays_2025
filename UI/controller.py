import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaAeroporti(self, e):
        input=self._view.txt_compagnieMinimo.value
        if input=="":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un numero minimo di compagnie", color="red"))
            self._view.update_page()
            return
        try:
            num_min = int(input)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico", color="red"))
            self._view.update_page()
            return

        self._view.txt_result.controls.clear()
        self._model.buildGraph(num_min)
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view._dd_aeroportoPartenza.disabled=False
        self._view._dd_aeroportoDest.disabled=False
        self.fill_dd()
        self._view.update_page()

    def handleTestConnessione(self, e):
        source=self._model.ottieni_nodo(self._view._dd_aeroportoPartenza.value)
        target=self._model.ottieni_nodo(self._view._dd_aeroportoDest.value)

        if source== target:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(
                "Aeroporto di Origine e Aeroporto Destinazione non possono coincidere!!", color="red"))
            self._view.update_page()
            return
        if not self._model.has_path(source, target):
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(
                "Non è stato trovata nessuna tratta tra i due aeroporti", color="red"))
            self._view.update_page()
            return
        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(
                "E' stato trovato almeno un collegamento tra i due aeroporti! "))
            self._view.txt_result.controls.append(ft.Text("Percorso minimo:"))
            percorso=self._model.percorso_minimo_djk(source, target)
            for i in percorso:
                self._view.txt_result.controls.append(ft.Text(i))
                self._view.txt_result.controls.append(ft.Text("-"*60))


            self._view.update_page()




    def fill_dd(self):
        self._view._dd_aeroportoPartenza.options.clear()
        self._view._dd_aeroportoDest.options.clear()

        nodi = self._model.elementi_dd()
        #print(len(nodi))
        for i in nodi:
            self._view._dd_aeroportoPartenza.options.append(ft.dropdown.Option(text=str(i), key=i.ID))
            self._view._dd_aeroportoDest.options.append(ft.dropdown.Option(text=str(i), key=i.ID))


        self._view._dd_aeroportoPartenza.update()
        self._view._dd_aeroportoDest.update()

        self._view.update_page()
