graph = {
    "A": ["S","Z","T"],
    "S": ["F","R"],
    "R": ["P"],
    "P": ["B"],
    "Z": ["O"],
    "O": ["S"],
    "T": ["L"],
    "L": ["M"],
    "M": ["D"],
    "D": ["C"],
    "C": ["P", "R"],
    "F": ["B"],
    "B": ["G","U"],
    "U": ["H","V"],
    "V": ["L"],
    "L": ["N"],
    "H": ["E"],
    "G":[],
    "E": [],
    "L":[]
}

def dfs(graph, start_node, goal_node):


    stack = [[start_node]]
    visited = []

    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal_node:
            return print("This is DFS Path", path)
                
        children = graph[node]
        for child in children:
            if child not in visited:
                newPath = path + [child]
                stack.insert(0, newPath)
                visited.append(child)



dfs(graph, "A", "B")