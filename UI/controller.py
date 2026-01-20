import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_album = int(self._view.txtNumAlbumMin.value)
        except ValueError:
            self._view.show_alert("Inserire un numero valido")
            return

        self._model.load_artists_with_min_albums(n_album)
        self._model.build_graph()

        # aggiorna dropdown album
        self._view.ddArtist.options = [ft.dropdown.Option(a.name) for a in self._model._artists_list_album]
        self._view.txt_result.controls.clear()

        self._view.ddArtist.disabled = False
        self._view.btnArtistsConnected.disabled = False
        self._view.update_page()


    def handle_connected_artists(self, e):
        pass



