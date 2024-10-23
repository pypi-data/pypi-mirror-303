class Node:
    def __init__(self, state, parent, action, total_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.total_cost = total_cost
        
def action_sequence(graph, initial_state, goal_state):
    solution = [goal_state]
    curr_parent = graph[goal_state].parent
    while curr_parent is not None:  # Add initial_state to the sequence
        solution.append(curr_parent)
        curr_parent = graph[curr_parent].parent
    solution.reverse()
    return solution


def bfs(): 
    initial_state = 'D'
    goal_state = 'C'
    graph = {
        'A' : Node('A', None, ['B', 'C','E'], None),
        'B' : Node('B', None, ['A', 'D', 'E'], None),
        'C' : Node('C', None, ['A', 'F', 'G'], None),
        'D' : Node('D', None, ['B', 'E'], None),
        'E' : Node('E', None, ['A', 'B', 'D'], None),
        'F' : Node('F', None, ['C'], None),
        'G' : Node('G', None, ['C'], None)
    }
    frontier = [initial_state]
    explored = []
    while len(frontier)!=0:
        current_node = frontier.pop(0)
        explored.append(current_node)
        for child in graph[current_node].action:
            if child not in explored and child not in frontier:
                graph[child].parent = current_node
                if graph[child].state == goal_state:
                    return action_sequence(graph, initial_state, goal_state)
                frontier.append(child)
    return None

solution = bfs()
print(solution)