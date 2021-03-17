from kruskal import Kruskal

nodes = ['a', 'd', 'f', 'b', 'c', 'e', 'g']
edges = [
    ['a', 'b', 7],
    ['b', 'c', 8],
    ['a', 'd', 5],
    ['d', 'b', 9],
    ['d', 'e', 15],
    ['d', 'f', 6],
    ['b', 'e', 7],
    ['f', 'e', 8],
    ['f', 'g', 11],
    ['e', 'g', 9],
    ['c', 'e', 5]
]
# Instanciamos la clase Kruskal y pasamos los datos
kruskal = Kruskal()
met = kruskal.apply_kruskal(edges, nodes)
# Podemos recorrer el arbol de expansión mínima
print("El camino obtenido es:")
print(met)
# Podemos saber el peso de el arbol
cost = sum([item[2] for item in met])
print(f"El costo de visitar todos los nodos es: {cost}")