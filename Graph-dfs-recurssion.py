class GraphNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_node(self, node):
        self.children.append(node)
    def remove_node(self,node):
        if node in self.children:
            self.children.reverse(node)

class Graph:
    def __init__(self, node_list):
        self.nodes = node_list
    def add_edge(self, node1, node2):
        node1.add_node(node2)
        node2.add_node(node1)
    def remove_edge(self, node1, node2):
        node1.remove_node(node2)
        node2.remove_node(node1)

nodeG = GraphNode("G")
nodeR = GraphNode("R")
nodeA = GraphNode("A")
nodeP = GraphNode("P")
nodeH = GraphNode("H")
nodeS = GraphNode("S")
graph = Graph([nodeG, nodeR, nodeA, nodeP, nodeH, nodeS])
graph.add_edge(nodeG, nodeR)
graph.add_edge(nodeR, nodeA)
graph.add_edge(nodeG, nodeA)
graph.add_edge(nodeR, nodeP)
graph.add_edge(nodeR, nodeS)
graph.add_edge(nodeG, nodeH)

# for each in graph.nodes:
#     print(each.value)
#     for child in each.children:
#         print("-->{}".format(child.value))
#     print("\n")

def dfs_recursion(root_node, search_value):
    return return_dfs_recursion(root_node, search_value, {})

def return_dfs_recursion(node, search_value, seen):
    if node == None:
       return False
    if node.value == search_value:
        return (node)
    seen[node.value] = True
    for each in node.children:
        if each.value not in seen:
            return return_dfs_recursion(each, search_value, seen)

assert dfs_recursion(nodeS, 'A') == nodeA
