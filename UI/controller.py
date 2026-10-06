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

    def handleStampaInfo(self, e):
        # PULISCO l'output precedente
        self._view._txt_result.controls.clear()

        # Prendo dal Model la lista delle componenti connesse
        cc = self._model.TotCompConnesse()

        # Il numero di componenti = lunghezza della lista
        self._view._txt_result.controls.append(
            ft.Text(f"Il grafo ha {len(cc)} componenti connesse")
        )

        # Trovo la componente connessa più grande
        largest = self._model.getLargestComp(cc)

        # La dimensione della componente = numero di album che contiene
        self._view._txt_result.controls.append(
            ft.Text(f"Dimensione della componente connessa più grande: {len(largest)} album")
        )

        # Stampo il titolo e il numero di brani di ogni album
        self._view._txt_result.controls.append(
            ft.Text("Dettagli degli album appartenenti alla componente connessa più grande:")
        )

        # ORDINO gli album alfabeticamente per titolo
        largest.sort(key=lambda a: a.Title)

        # Scorro gli album uno alla volta
        for a in largest:
            self._view._txt_result.controls.append(
                ft.Text(f"- {a.Title}: {len(a.Tracks)} brani")
            )

        # Aggiorno la pagina per visualizzare i risultati
        self._view.update_page()
    def handleSelezione(self,e):
        pass