from .main import recursive_best_first_search



# # Heuristic distances for each node
# H_dist = {
#     'S': 5,
#     'A': 3,
#     'B': 4,
#     'C': 2,
#     'D': 6,
#     'G': 0,
# }

# # Graph representation
# Graph_nodes = {
#     'S': [('A', 1), ('G', 10)],
#     'A': [('B', 2), ('C', 1)],
#     'B': [('D', 5)],
#     'C': [('D', 3), ('G', 4)],
#     'D': [('G', 2)],
#     'G': None
# }

# recursive_best_first_search(Graph_nodes, H_dist, 'S', 'G')