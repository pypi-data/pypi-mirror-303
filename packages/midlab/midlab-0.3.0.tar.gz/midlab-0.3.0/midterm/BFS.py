graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : ['I'],
    'F' : [],
    'G' : ['J'],
    'H' : [],
    'I' : [],
    'J' : []
}

visited = []
queue = []

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end= " ")

        if m == goal:
            print('Goal reached:')
            return

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print('Result')
bfs(visited, graph, 'A', 'D')