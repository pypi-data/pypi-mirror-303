graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': ['I', 'J'],
    'H': [],
    'I': [],
    'J': []
}

def dfs(graph, start_node, goal_node):


    stack = [[start_node]]#[c,b,a,]
    visited = [] #b,c,f,g

    while stack:
        path = stack.pop()#c
        node = path[-1]#
        if node == goal_node:
            return print("This is DFS Path", path)
                
        children = graph[node]
        for child in children:
            if child not in visited:
                newPath = path + [child]#f,
                print(newPath)
                stack.insert(0, newPath)
                visited.append(child)



dfs(graph, "A", "G")