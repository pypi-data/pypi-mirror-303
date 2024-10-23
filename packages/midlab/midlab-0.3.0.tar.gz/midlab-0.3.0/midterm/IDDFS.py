graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'G': ['H'],
    'F': [],
    'H': [],
}

path = list()  # This will store the final correct path

def DFS(start, goal, graph, maxDepth, curList):
    print("The Route of IDFS is", start)
    curList.append(start)  # Append current node to the path
    
    if start == goal:
        path.extend(curList)  # Save the found path
        return True
    
    if maxDepth <= 0:
        return False
    
    for node in graph[start]:
        if DFS(node, goal, graph, maxDepth - 1, curList):
            return True
        
    curList.pop()  # Backtrack
    return False

def IDDFS(start, goal, graph, maxDepth):
    for i in range(maxDepth + 1):
        print("New Iteration at depth:", i)
        curList = list()
        if DFS(start, goal, graph, i, curList):
            return True
    return False

if not IDDFS('A', 'E', graph, 3):
    print("Path does not exist")
else:
    print("A path is", path)