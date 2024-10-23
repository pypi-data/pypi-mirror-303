graph = {
    'A': ['Z', 'S', 'T'],
    'Z': ['A', 'O'],
    'S': ['A', 'F', 'R'],
    'T': ['A', 'L'],
    'O': ['Z', 'S'],
    'F': ['S', 'B'],
    'R': ['S', 'P', 'C'],
    'L': ['T', 'M'],
    'B': ['F', 'G', 'U', 'P'],
    'P': ['R', 'B', 'C'],
    'C': ['R', 'D', 'P'],
    'M': ['L', 'D'],
    'G': ['B'],
    'U': ['B', 'V', 'H'],
    'D': ['C', 'M'],
    'V': ['U', 'I'],
    'H': ['U', 'E'],
    'I': ['V', 'N'],
    'E': ['H'],
    'N': ['I']
}

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = [[start]]
    if start == goal:
        return [start]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbors = graph[node]
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    return new_path
            
            visited.add(node)
    
    return None

start = 'A'
goal = 'B'
shortest_path = bfs_shortest_path(graph, start, goal)

if shortest_path:
    print(shortest_path)
else:
    print(f"No path found from {start} to {goal}")