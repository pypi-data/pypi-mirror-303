# A* With Cost in result
graph = {
    'S': {'A': 1, 'B': 5, 'C': 8},
    'A': {'S': 1, 'D': 3, 'E': 7, 'G': 9},
    'B': {'S': 5, 'G': 4},
    'C': {'S': 8, 'G': 5},
    'D': {'A': 3},
    'E': {'A': 7}
}

# Heuristic (estimated cost from each node to the goal)
heuristic = {
    'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0
}

def Astar(graph,start,end):
    queue=[(0,start)]
    gcost={start:0}
    visited={start:None}
    while queue:
        queue.sort(key=lambda x:x[0])
        currentCost,currentNode=queue.pop(0)
        if currentNode==end:
            path=[]
            while currentNode:
                path.append(currentNode)
                currentNode=visited[currentNode]
            return currentCost,path[::-1]
        for neighbor,cost in graph[currentNode].items():
            fcost=gcost[currentNode]+cost
            if neighbor not in visited or fcost<gcost[neighbor]:
                gcost[neighbor]=fcost
                totalCost=fcost+heuristic[neighbor]
                queue.append((totalCost,neighbor))
                visited[neighbor]=currentNode
    return None

start="S"
end="G"
result=Astar(graph,start,end)
if result:
    cost,path=result
    print("Path",path)
    print("Cost",cost)
else:
    print("Not found")