import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'{self._model._graph}'))
        self._view.update_page()

    def handleCompConnessa(self,e):
        obj_id = self._view._txtIdOggetto.value

        try:
            id = int(obj_id)
            num = self._model.calcolaConnessa(id)

            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Dim. componente connessa: {num}'))

            self.populate_dd(num)

            self._view.update_page()
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text('Inserire un valore valido!'))
            self._view.update_page()

    def handleCercaOggetti(self, e):
        lunghezza = int(self._view._ddLunghezza.value)
        soluzione, peso = self._model.cercaOggetti(lunghezza)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Il peso totale vale: {peso}.'))
        for v in soluzione:
            self._view.txt_result.controls.append(ft.Text(f'{v}'))
        self._view.update_page()


    def populate_dd(self, num):
        self._view._ddLunghezza.options.clear()
        for i in range(2, num):
            self._view._ddLunghezza.options.append(ft.DropdownOption(key=str(i), text=str(i)))
