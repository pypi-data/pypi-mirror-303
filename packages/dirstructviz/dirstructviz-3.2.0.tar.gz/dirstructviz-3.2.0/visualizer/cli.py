import click
from visualizer.tree_builder import build_tree
from visualizer.exporter import export_directory_structure

@click.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False))
@click.option('--max-depth', default=-1, help='Maximum depth of the directory tree.')
@click.option('--export', type=click.Choice(['ascii', 'matplotlib', 'networkx'], case_sensitive=False), help='Format to export the directory structure.')
@click.option('--output', type=click.Path(), help='Output file path.')
def visualize(path, max_depth, export, output):
    tree = build_tree(path, max_depth=max_depth)
    if export:
        export_directory_structure(tree, export_format=export, output_path=output)
    else:
        # Default to ASCII if no export option is provided
        export_directory_structure(tree, export_format='ascii')

if __name__ == '__main__':
    visualize()
