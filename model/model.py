import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list_album = []


    def load_artists_with_min_albums(self, min_albums):
         self._artists_list_album = DAO.get_artists_album(min_albums)
         return self._artists_list_album



    def build_graph(self):
        self._graph.clear()

        for a in self._artists_list_album:
            self._graph.add_node(a)

    def get_connected_artists(self, artista):
        artista_start = artista
        if artista_start not in self._graph:
            return []
        return list(nx.node_connected_component(self._graph, artista_start))



