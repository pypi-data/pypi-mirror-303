import heapq


def uniform_cost_search(graph, start, goal):
    # Priority queue to store the frontier nodes, initialized with the start node
    priority_queue = [(0, start)]
    # Dictionary to store the cost of the shortest path to each node
    visited = {start: (0, None)}

    while priority_queue:
        # Pop the node with the lowest cost from the priority queue
        current_cost, current_node = heapq.heappop(priority_queue)

        # If we reached the goal, return the total cost and the path
        if current_node == goal:
            return current_cost, reconstruct_path(visited, start, goal)

        # Explore the neighbors
        for neighbor, cost in graph[current_node]:
            total_cost = current_cost + cost
            # Check if this path to the neighbor is better than any previously found
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor] = (total_cost, current_node)
                heapq.heappush(priority_queue, (total_cost, neighbor))

    # If the goal is not reachable, return None
    return None


def reconstruct_path(visited, start, goal):
    # Reconstruct the path from start to goal by following the visited nodes
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1]  # Get the parent node
    path.reverse()
    return path


# Example graph represented as an adjacency list
graph = {
    "A": [("S", 140), ("Z", 75), ("T", 118)],
    "S": [("F", 99), ("R", 80)],
    "R": [("P", 97), ("C", 146)],
    "P": [("B", 101)],
    "Z": [("O", 71)],
    "O": [("S", 151)],
    "T": [("L", 111)],
    "L": [("M", 70)],
    "M": [("D", 75)],
    "D": [("C", 120)],
    "C": [("P", 138), ("R", 146)],
    "F": [("B", 211)],
    "B": [("G", 90), ("U", 85)],
    "U": [("H", 98), ("V", 142)],
    "V": [("La", 92)],
    "La": [("N", 87)],
    "H": [("E", 86)],
    "G": [],
    "E": [],
    "N": [],
}

# Example usage of the UCS function
start_node = "A"
goal_node = "N"
result = uniform_cost_search(graph, start_node, goal_node)

if result:
    total_cost, path = result
    print(
        f"Least cost path from {start_node} to {goal_node}: {' -> '.join(path)} with total cost {total_cost}"
    )
else:
    print(f"No path found from {start_node} to {goal_node}")
