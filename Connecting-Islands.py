import heapq


def graph(bridge_config, num_islands):
    adjecency_list = [list() for _ in range(num_islands+1)]
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        adjecency_list[source].append((destination, cost))
        adjecency_list[destination].append((source, cost))
    print(adjecency_list)
    return adjecency_list

def minimum_cost(graph):
    visited = [False for _ in range(len(graph)+1)]
    start_vertex = 1
    heap = [(0, start_vertex)]
    total = 0
    while len(heap)>0:
        cost, current_vertex = heapq.heappop(heap)
        if visited[current_vertex] == True:
            continue
        total += cost
        for neighbor, cost in graph[current_vertex]:
            heapq.heappush(heap, (cost, neighbor))
        visited[current_vertex] = True
    return total


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
graph = graph(bridge_config, num_islands)
cost = minimum_cost(graph)
print(cost)
