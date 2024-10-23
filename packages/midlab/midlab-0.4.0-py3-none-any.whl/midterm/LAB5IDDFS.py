graph = {
    "A": ["S", "Z", "T"],
    "S": ["F", "R"],
    "R": ["P","C"],
    "P": ["B"],
    "Z": ["O"],
    "O": ["S"],
    "T": ["L"],
    "L": ["M"],
    "M": ["D"],
    "D": ["C"],
    "C": ["P", "R"],
    "F": ["B"],
    "B": ["G", "U"],
    "U": ["H", "V"],
    "V": ["La"],
    "La": ["N"],
    "H": ["E"],
    "G": [],
    "E": [],
    "L": [],
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


if not IDDFS("A", "L", graph, 3):
    print("Path does not exist")
else:
    print("A path is", path)
