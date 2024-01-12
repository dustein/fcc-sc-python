#os system comando limpar a tela sempre ue rodar
import os
os.system('clear')

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
  # unvisited = []
  # distances = {}
  # for node in graph:
  #   unvisited.append(node)
  #   if node == start:
  #     distances[node] = 0
  #   else:
  #     distances[node] = float('inf')
  unvisited = list(graph)
  distances = {node: 0 if node == start else float('inf') for node in graph }
  paths = {node: [] for node in graph}
  paths[start].append(start)

  while unvisited:
    current = min(unvisited, key=distances.get)
    for node, distance in graph[current]:
      pass
  print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

shortest_path(my_graph, 'A')