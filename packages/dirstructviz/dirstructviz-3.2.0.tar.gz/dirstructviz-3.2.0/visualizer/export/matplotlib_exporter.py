import matplotlib.pyplot as plt

def export_to_matplotlib(tree, output_path=None):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title(f"Directory Structure", fontsize=16)
    ax.axis("off")
    
    def draw_node(ax, label, x, y):
        ax.text(x, y, label, fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    def add_nodes(ax, node, x, y, spacing):
        draw_node(ax, node.name, x, y)
        step = spacing / len(node.children) if node.children else 1
        for i, child in enumerate(node.children):
            new_x = x - spacing / 2 + step * (i + 0.5)
            new_y = y - 1
            ax.plot([x, new_x], [y - 0.1, new_y + 0.1], 'k-')
            add_nodes(ax, child, new_x, new_y, spacing / 2)

    # Start plotting
    draw_node(ax, tree.name, 0, 0)
    add_nodes(ax, tree, 0, 0, 10)

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
