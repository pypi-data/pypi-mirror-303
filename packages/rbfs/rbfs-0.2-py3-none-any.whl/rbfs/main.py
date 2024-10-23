from queue import PriorityQueue


def recursive_best_first_search(graph, H_dist, current_node, target, visited=set(), current_cost=0, parent={}):
    if current_node=='S':
        parent[current_node] = None
    # Base case: if we reach the target
    if current_node == target:
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]
        path.reverse()

        print(f"Optimal path: {' -> '.join(path)}")
        print(f"Total cost: {current_cost}")
        return True

    visited.add(current_node)

    # Create a list of neighbors with their costs
    neighbors = graph.get(current_node, [])

    # Sort neighbors based on heuristic cost
    neighbors.sort(key=lambda x: (current_cost + x[1] + H_dist[x[0]]))

    # Explore neighbors
    for neighbor, cost in neighbors:
        if neighbor not in visited:
            parent[neighbor] = current_node
            total_cost = current_cost + cost

            # Recursive call
            if recursive_best_first_search(graph, H_dist, neighbor, target, visited, total_cost):
                return True

            # Backtrack
            del parent[neighbor]

    return False

# def best_first_search(graph, H_dist, source, target):
#     visited = set()  # To keep track of visited nodes
#     parent = {source: None}  # To reconstruct the path
#     recursive_best_first_search(graph, H_dist, source, target, visited, 0, parent)

