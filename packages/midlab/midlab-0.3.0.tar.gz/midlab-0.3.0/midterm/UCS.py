import heapq

def ucs(graph, start, goal):
    # Priority queue to store (cost, node)
    queue = [(0, start)]
    # Dictionary to store the cost of reaching each node
    visited = {start: (0,None)}
    
    while queue:
        # Get the node with the lowest cost
        cost, node = heapq.heappop(queue)
        
        # If we've reached the goal, return the cost
        if node == goal:
            return cost,reconstruct_path(visited,goal)
        
        # Explore neighbors
        for child, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            
            # If the child hasn't been visited or a cheaper path is found
            if child not in visited or new_cost < visited[child][0]:
                visited[child] = (new_cost,node)
                heapq.heappush(queue, (new_cost, child))
    
    # If no path to the goal is found
    return float('inf')


def reconstruct_path(visited, goal):
    path = []
    while goal:
        path.append(goal)
        goal = visited[goal][1]
    return path[::-1]


# Example graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Running UCS from A to G
start = 'A'
goal = 'G'
result = ucs(graph, start, goal)

if result != float('inf'):
    print(f"Lowest cost to get from {start} to {goal}: {result}")
else:
    print(f"No path found from {start} to {goal}")
