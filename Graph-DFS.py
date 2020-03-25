class GraphNode: 
    def __init__(self,value):
        self.value = value
        self.children = []
    def add_node (self, new_node):
        self.children.append(new_node)
    def remove_node (self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph:
    def __init__(self, node_list):
        self.nodes = node_list
    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_node(node2)
            node2.add_node(node1)
    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_node(node2)
            node2.remove_node(node1)

nodeG = GraphNode("G")
nodeR = GraphNode("R")
nodeA = GraphNode("A")
nodeP = GraphNode("P")
nodeH = GraphNode("H")
nodeS = GraphNode("S")

graph1 = Graph([nodeG, nodeR, nodeA, nodeP, nodeH, nodeS])
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

def dfs_search(root_node, search_value):
    seen = []
    stack = [root_node]
    while len(stack) > 0:
        current_node = stack.pop()
        seen.append(current_node)
        if current_node.value == search_value:
            return current_node
        for child in current_node.children:
            if child not in seen and child not in stack:
                stack.append(child)

assert nodeA == dfs_search(nodeG, 'A')
assert nodeA == dfs_search(nodeS, 'A')
assert nodeS == dfs_search(nodeP, 'S')
assert nodeR == dfs_search(nodeH, 'R')
