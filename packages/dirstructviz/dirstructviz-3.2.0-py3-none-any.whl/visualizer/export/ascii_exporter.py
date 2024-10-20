from rich.tree import Tree
from rich.console import Console

def export_to_ascii(tree, output_path=None):
    """
    Export the directory structure as ASCII art.

    :param tree: The directory tree.
    :param output_path: Path to save the text file, or None to print to the console.
    """
    console = Console()
    rich_tree = Tree(tree.name)
    add_nodes_to_rich_tree(tree, rich_tree)

    if output_path:
        with open(output_path, 'w') as file:
            console = Console(file=file)
            console.print(rich_tree)
    else:
        console.print(rich_tree)

def add_nodes_to_rich_tree(node, rich_node):
    for child in node.children:
        new_rich_node = rich_node.add(child.name)
        if child.is_dir:  # Use 'is_dir' as a boolean attribute, not a method
            add_nodes_to_rich_tree(child, new_rich_node)
