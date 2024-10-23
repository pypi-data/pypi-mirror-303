from collections import deque
maze = [
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

start = (3, 3) 
end = (0, 5)   

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    parent = {start: None}

    while queue:
        current = queue.popleft()
        
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            row, col = neighbor
            
            if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    
    return []  

path = bfs(maze, start, end)
print("Path from start to goal:", path)
