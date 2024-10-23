
import heapq

def a_star(graph, heuristics, start, goal):
    def heuristic(node):
        return heuristics[node]
    
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start), 0, start, [start]))
    closed_list = set()
    
    while open_list:
        _, cost, current, path = heapq.heappop(open_list)
        
        if current in closed_list:
            continue
        
        if current == goal:
            return path, cost
        
        closed_list.add(current)
        
        for neighbor, weight in graph[current]:
            if neighbor in closed_list:
                continue
            new_cost = cost + weight
            heapq.heappush(open_list, (new_cost + heuristic(neighbor), new_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')

# Define the graph as a dictionary
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('G', 1),('E', 6)],
    'E': [('A', 3),('D', 6)],
    'G': [('D', 1),('B', 9)]
}

# Define the heuristics for each node
heuristics = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

start = 'A'
goal = 'G'
path, cost = a_star(graph, heuristics, start, goal)
print("Optimal path:", path)
print("Optimal path cost:", cost)
