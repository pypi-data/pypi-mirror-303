# graph = {
#     "A": ["S", "Z", "T"],
#     "S": ["F", "R"],
#     "R": ["P","C"],
#     "P": ["B"],
#     "Z": ["O"],
#     "O": ["S"],
#     "T": ["L"],
#     "L": ["M"],
#     "M": ["D"],
#     "D": ["C"],
#     "C": ["P", "R"],
#     "F": ["B"],
#     "B": ["G", "U"],
#     "U": ["H", "V"],
#     "V": ["La"],
#     "La": ["N"],
#     "H": ["E"],
#     "G": [],
#     "E": [],
#     "L": [],
# }

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "G": ["J"],
    "F": [],
    "H": [],
    "I": [],
    "J": [],
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


dfs(graph, "A", "G")


# class Node:
#     def __init__(self, state, parent, actions, totalCost):
#         self.state = state
#         self.parent = parent
#         self.actions = actions
#         self.totalCost = totalCost


# def actionSequence(graph, initialState, goalState):
#     solution = [goalState]
#     currentParent = graph[goalState].parent

#     while currentParent != None:
#         solution.append(currentParent)
#         currentParent = graph[currentParent].parent

#     solution.reverse()

#     return solution


# def DFS():
#     initialState = "A"
#     goalState = "G"

#     graph = {
#         "A": Node("A", None, ["B", "E", "C"], None),
#         "B": Node("B", None, ["D", "E", "A"], None),
#         "C": Node("C", None, ["A", "F", "G"], None),
#         "D": Node("D", None, ["B", "E"], None),
#         "F": Node("F", None, ["C"], None),
#         "G": Node("G", None, ["C"], None),
#     }

#     frontier = [initialState]
#     explored = []
#     while len(frontier) != 0:
#         currentNode = frontier.pop(len(frontier) - 1)
#         print(currentNode)
#         explored.append(currentNode)
#         currentChildren = 0

#         for child in graph[currentNode].actions:
#             if child not in frontier and child not in explored:
#                 graph[child].parent = currentNode
#                 if graph[child].state == goalState:
#                     print("Goal State Reached", explored)
#                     return actionSequence(graph, initialState, goalState)
#                 currentChildren = currentChildren + 1
#                 frontier.append(child)

#         if currentChildren == 0:
#             del frontier[len(frontier) - 1]

# solution = DFS()
# print(solution)