import networkx as nx
import matplotlib.pyplot as plt

def export_to_networkx(tree, output_path=None):
    graph = nx.DiGraph()
    
    def add_edges(node, parent=None):
        graph.add_node(node.name)
        if parent:
            graph.add_edge(parent.name, node.name)
        for child in node.children:
            add_edges(child, node)

    add_edges(tree)
    
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
    
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
