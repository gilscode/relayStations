"""
Este ficheiro serve só para eu fazer debug ao código que faço.
- Gil
"""

from filesReading import *
from Graph import *

from pathCalculator import *

graph = readStations('grafoAvaliacao.txt')

nodeA = graph.getNodeByName('Davia')
nodeB = graph.getNodeByName('Uige')


# for i in requests:
#     print('(')
#     for j in i:
#         print(j)
#     print(')')

outSearch = search(graph, nodeA, nodeB)
print('Best Path:')
print(printPath(outSearch[0]))
print('Best Time:')
print(outSearch[1])




