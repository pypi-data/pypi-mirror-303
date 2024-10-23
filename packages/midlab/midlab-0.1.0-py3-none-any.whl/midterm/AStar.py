tree = {
    "A": [["B", 2], ["E", 3]],
    "B": [["C", 1], ["G", 9]],
    "E": [["D", 6]],
    "D": [["G", 1]],
    "C": [],
    "G": [],
}

heuristic = {"A": 11, "B": 6, "C": 99, "D": 1, "E": 7, "G": 0}

cost = {"A": 11}


def AStarSearch():
    global tree, heuristic
    closed = []
    opened = [["A", 11]]

    while True:
        fn = [i[1] for i in opened]
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == "G":
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + item[1]
            temp = [item[0], fn_node]
            opened.append(temp)

    trace_node = "G"
    optimal_sequence = ["G"]
    for i in range(len(closed) - 2, -1, -1):
        check_node = closed[i][0]
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            if (
                cost[check_node] + children_costs[children_nodes.index(trace_node)]
                == cost[trace_node]
            ):
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()

    return closed, optimal_sequence


if __name__ == "__main__":
    visited_nodes, optimal_nodes = AStarSearch()
    print("visited nodes: " + str(visited_nodes))
    print("optimal nodes sequence: " + str(optimal_nodes))
