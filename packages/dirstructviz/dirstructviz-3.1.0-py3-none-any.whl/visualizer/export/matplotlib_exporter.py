import matplotlib.pyplot as plt

def export_to_matplotlib(tree, output_path=None):
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_title("Directory Structure", fontsize=16)
    ax.axis("off")

    # Recursively draw the nodes with proper spacing
    def draw_node(ax, label, x, y):
        ax.text(x, y, label, fontsize=10, ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    def add_nodes(ax, node, x, y, level=0):
        spacing = 3.0 / (level + 1)  # Dynamically calculate horizontal spacing based on level
        draw_node(ax, node.name, x, y)
        num_children = len(node.children)
        child_y = y - 1.5  # Increase vertical space between levels

        for i, child in enumerate(node.children):
            # Adjust x position based on index of the child node
            child_x = x - spacing * (num_children / 2) + spacing * (i + 0.5)
            ax.plot([x, child_x], [y - 0.1, child_y + 0.1], 'k-')
            add_nodes(ax, child, child_x, child_y, level + 1)

    # Start plotting from the root node
    add_nodes(ax, tree, 0, 0)

    if output_path:
        plt.savefig(output_path, bbox_inches='tight')
    else:
        plt.show()
