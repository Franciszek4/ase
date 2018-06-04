from math import inf
from time import sleep

graph = {'a': [inf, inf, 1, 2, inf, inf, inf],
         'b': [inf, inf, 2, inf, inf, 3, inf],
         'c': [1, 2, inf, 1, 3, inf, inf],
         'd': [2, inf, 1, inf, inf, inf, 1],
         'e': [inf, inf, 3, inf, inf, 2, inf],
         'f': [inf, 3, inf, inf, 2, inf, 1],
         'g': [inf, inf, inf, 1, inf, 1, inf]}


nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
distances = [inf, inf, inf, inf, inf, inf, inf]
previous = ['', '', '', '', '', '', '']
available = [True, True, True, True, True, True, True]

num_of_nodes = 7


finish = False
source = 'a'
destination = 'f'
start = source
previous_node = destination
destination_ind = nodes.index(destination)
source_ind = nodes.index(source)

available[source_ind] = False
distances = graph[source]
previous[source_ind] = source

for i in range(0, num_of_nodes):
    if graph[source][i] < inf:
        previous[i] = source

while not finish:
    min_index = 0
    min_value = inf
    for i in range(0, num_of_nodes):
        if distances[i] < min_value and available[i]:
            min_value = distances[i]
            min_index = i

    min_dist_neighbour = min_index
    available[min_dist_neighbour] = False

    source = nodes[min_dist_neighbour]
    source_ind = min_dist_neighbour

    for i in range(0, num_of_nodes):
        if available[i]:
            if graph[source][i] + distances[source_ind] < distances[i]:
                distances[i] = graph[source][i] + distances[source_ind]
                previous[i] = source

    if True not in available:
        finish = True

idx_path = []
while previous_node != start:
    idx_path.append(nodes.index(previous_node))
    previous_node = previous[nodes.index(previous_node)]

idx_path.append(nodes.index(start))
path = []
for i in range(0, len(idx_path)):
    path.append(nodes[idx_path[i]])

path.reverse()
print(path)
