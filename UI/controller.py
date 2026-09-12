import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self, e):
        # ATTENZIONE ARRIVA UNA LISTA DA MODEL.PY
        # e per il numero di nodi devo stampare un numero quindi uso len
        self._model.buildGraph()
        # devo costruire il grafo
        self._view._txt_result.controls.clear()
        # comando per aggiungere righe testuali/numero in output
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi:{self._model.getNodes()}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi:{self._model.getEdges()}"))


        self._view.update_page()

    def handleStampaInfo(self,e):
        self._view._txt_result.controls.clear()
        cc = self._model.TotCompConnesse()
        # quante componenti ci sono? -> len(lista)
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {len(cc)} componenti connesse"))
        # largest contiene la lista con più attori (l'insieme che contiene più nodi/attori)
        largest = self._model.getLargestComp(cc)
        self._view._txt_result.controls.append(ft.Text(f"Dimensione della componente connessa più grande: {len(largest)} album"))
        # cambia valore a ogni giro del ciclo. a=luca stampa a.Name "luca"
        # e quindi li prende ad uno  ad uno i valori(attori) della lista
        #self._view.txt_result.controls.append(ft.Text("Dettagli degli album appartenenti alla conponente connessa più grande:"
        self._view._txt_result.controls.append(ft.Text ("Dettagli degli album appartenenti alla componenti connessa più grande:"))
        for a in largest:
            self._view._txt_result.controls.append(
                ft.Text(f"-{a.Title}: {len(a.Tracks)} brani"))

        self._view.update_page()

    def handleSelezione(self,e):
        pass