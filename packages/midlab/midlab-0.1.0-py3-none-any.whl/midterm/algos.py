import heapq

def uniform_cost_search(graph, start, goal):
    """
    Performs Uniform Cost Search (UCS) on the given graph to find the least-cost path.

    :param graph: A dictionary where keys are node names and values are lists of (neighbor, cost) tuples.
    :param start: The starting node for the search.
    :param goal: The goal node to search for.
    :return: A tuple containing the total cost and the least-cost path, or None if the goal is not reachable.
    """

    # Priority queue to store the frontier nodes, initialized with the start node
    priority_queue = [(0, start)]
    # Dictionary to store the cost of the shortest path to each node
    visited = {start: (0, None)}

    while priority_queue:
        # Pop the node with the lowest cost from the priority queue
        current_cost, current_node = heapq.heappop(priority_queue)

        # If we reached the goal, return the total cost and the path
        if current_node == goal:
            return current_cost, _reconstruct_path(visited, start, goal)

        # Explore the neighbors
        for neighbor, cost in graph.get(current_node, []):
            total_cost = current_cost + cost
            # Check if this path to the neighbor is better than any previously found
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor] = (total_cost, current_node)
                heapq.heappush(priority_queue, (total_cost, neighbor))

    # If the goal is not reachable, return None
    return None

def _reconstruct_path(visited, start, goal):
    """
    Reconstructs the path from start to goal by following the visited nodes.

    :param visited: A dictionary mapping nodes to (cost, parent) tuples.
    :param start: The starting node of the path.
    :param goal: The goal node of the path.
    :return: The reconstructed path as a list of nodes.
    """
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1]  # Get the parent node
    path.reverse()
    return path
