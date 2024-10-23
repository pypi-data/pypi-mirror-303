import random

# Define a simple graph structure using a dictionary
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'D': 4, 'E': 5},
    'C': {'A': 2, 'F': 1},
    'D': {'B': 4},
    'E': {'B': 5},
    'F': {'C': 1}
}

# Define values associated with each node
node_values = {
    'A': 1,
    'B': 5,
    'C': 3,
    'D': 6,
    'E': 4,
    'F': 2
}

def hill_climbing(graph, start_node, goal_node):
    """Perform hill climbing search and return the path to the goal or local maximum."""
    current_node = start_node
    current_value = node_values[current_node]
    path = [current_node]  # To store the path taken
    
    while current_node != goal_node:
        neighbors = graph.get(current_node, {})  # Get neighbors of the current node
        next_node = None
        next_value = current_value

        # Look for the neighbor with the highest value
        for neighbor in neighbors:
            if node_values[neighbor] > next_value:
                next_value = node_values[neighbor]
                next_node = neighbor

        # If a better neighbor is found, move to that neighbor
        if next_node is not None and next_value > current_value:
            current_node = next_node
            current_value = next_value
            path.append(current_node)  # Add the node to the path
        else:
            # No better neighbor found or stuck in a local maximum, stop the search
            break

    # Return the found node, its value, and the path
    return current_node, current_value, path

# Example usage
start_node = 'B'
goal_node = 'D'
best_node, best_value, path = hill_climbing(graph, start_node, goal_node)

if best_node == goal_node:
    print(f"Goal node {goal_node} reached with value: {best_value}")
else:
    print(f"Local maximum reached at node {best_node} with value: {best_value}, goal not reached.")

print(f"Path taken: {' -> '.join(path)}")
