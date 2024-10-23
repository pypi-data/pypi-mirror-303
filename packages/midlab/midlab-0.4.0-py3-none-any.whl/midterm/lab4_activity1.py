class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost



def DFS():
    initial_state = 'A'
    goal_state = 'G'
    graph = {
    'A': Node('A', None, ['B','F', 'C'], None),
    'B': Node('B', None, ['D', 'E', 'A'], None),
    'C': Node('C', None, ['A', 'F', 'G'], None),
    'D': Node('D', None, ['B',  'E'], None),
    'E': Node('E', None, ['A', 'B', 'D'], None),
    'F': Node('F', None, ['C'], None),
    'G': Node('G', None, ['C'], None)
}
    frontier = [initial_state]
    explored = []
    while len(frontier) !=0:
        currentNode =   frontier.pop(len(frontier)-1)
        print(currentNode)
        explored.append(currentNode)
        currentChildren = 0
        for child in graph[currentNode].action:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if graph[child].state == goal_state:
                    print(explored)
                    return actionSequence(graph, initial_state, goal_state)
                currentChildren = currentChildren + 1
                frontier.append(child)
        if currentChildren == 0:
            del explored[len(explored)-1]
            
def actionSequence(graph, initial_state, goal_state):
    solution = [goal_state]
    currParent = graph[goal_state].parent
    while currParent != None:
        solution.append(currParent)
        currParent = graph[currParent].parent
    solution.reverse()
    return solution

solution = DFS()
print(solution)