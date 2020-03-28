import math
class GraphEdge:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edge = []
    def add_child(self, node, distance):
        self.edge.append(GraphEdge(node, distance))
    def remove_child(self, node):
        if node in self.edge:
            self.edge.remove(node)
class Graph:
    def __init__(self, node_list):
        self.nodes = node_list
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)
    def remove_edge(self, node1, node2):
        if node2 in self.nodes and node1 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

nodeU = GraphNode("U")
nodeD = GraphNode("D")
nodeA = GraphNode("A")
nodeC = GraphNode("C")
nodeI = GraphNode("I")
nodeT = GraphNode("T")
nodeY = GraphNode("Y")
graph = Graph([nodeU,nodeD,nodeA,nodeC,nodeI,nodeT,nodeY])
graph.add_edge(nodeU, nodeA, 4)
graph.add_edge(nodeU, nodeC, 6)
graph.add_edge(nodeU, nodeD, 3)
graph.add_edge(nodeD, nodeC, 4)
graph.add_edge(nodeC, nodeI, 4)
graph.add_edge(nodeC, nodeT, 5)
graph.add_edge(nodeI, nodeA, 7)
graph.add_edge(nodeI, nodeY, 4)
graph.add_edge(nodeT, nodeY, 5)

dictionary = {}
for node in graph.nodes:
    dictionary[node] = node.edge
    
def get_smallest_distance(seen, distance):
    temp_dis = 9999999
    temp_node = ""
    for node, dis in distance.items():
        if dis < temp_dis and node not in seen:
            temp_dis = dis
            temp_node = node
    return temp_node

def diijkstra(dict, start_node, end_node):
    current = start_node
    seen = []
    distance = {}
    distance[start_node.value] = 0

    #setting distance of direct nodes
    for edge in start_node.edge:
        distance[edge.node.value] = edge.distance

    while current.value not in seen :
        seen.append(current.value)
        for each in current.edge:
            node_dist = each.distance
            node = each.node.value
            if node not in seen:
                if node not in distance.keys():
                    distance[node] = node_dist + distance[current.value]
                elif distance[node] > distance[current.value] + node_dist:
                    distance[node] = distance[current.value] + node_dist

        #get node having smalllest distance 
        smallest_dis_node = get_smallest_distance(seen, distance)

        #setting current value to the node having smallest distance
        for node in graph.nodes:
            if node.value == smallest_dis_node:
                current = node
                break
        print(distance)

    return distance[end_node.value]


print("Pass" if diijkstra(dictionary, nodeU, nodeY) == 14 else "Fail")