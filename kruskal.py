class Kruskal:

    def __init__(self):
        self.nodes = {}
        self.order = {}


    def prepare_data(self, node):
        # Buscamos dentro de los nodos aquel valor ingresado, en caso de no existir se crea el dato
        self.nodes[node] = node
        # Inicializar el orden respecto al nodo ingresado
        self.order[node] = 0


    def find_node(self, node):
        # Nos aseguramos de que el nodo presente en la llave "nodo" es igual valor del nodo ingresado
        if self.nodes[node] != node:
            self.nodes[node] = self.find_node(self.nodes[node])
        # Cuando encontramos el valor correcto según la llave lo retornamos y rompemos la recursividad
        return self.nodes[node]


    # Este es el método más importante del algoritmo
    def check_union(self, origin, arrival):
        origin_temp = self.find_node(origin)
        arrival_temp = self.find_node(arrival)
        if origin_temp != arrival_temp:
            if self.order[origin_temp] > self.order[arrival_temp]:
                self.nodes[arrival_temp] = origin_temp
            else:
                self.nodes[origin_temp] = arrival_temp
                if self.order[origin_temp] == self.order[arrival_temp]:
                    self.order[arrival_temp] += 1


    def get_weight(self, edge):
        return edge[2]


    # El formato de los nodos será el siguiente: ['a', 'b', 'c'...]
    # El formato de las aristas será: [['origen', 'destino', peso],[....], ...]
    def apply_kruskal(self, edges, nodes):
        # Declaramos e inicializamos el árbol de expansión mínima
        min_exp_tree = []
        # Recorrer todos los nodos y los insertamos al diccionario previamente creado
        for node in nodes:
            self.prepare_data(node)
        # Ordernar las aristas según su peso para facilitar la implementación de Kruskal
        edges.sort(key=self.get_weight)
        # Recorremos las aristas una vez ordenadas
        for edge in edges:
            origin, arrival, weight = edge
            if self.find_node(origin) != self.find_node(arrival):
                self.check_union(origin, arrival)
                min_exp_tree.append(edge)
        # Una vez ordenados y visitados los nodos, se adjuntan al árbol y se retorna el mismo
        return min_exp_tree
