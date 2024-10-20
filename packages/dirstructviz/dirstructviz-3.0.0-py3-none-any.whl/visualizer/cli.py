import click
from visualizer.tree_builder import build_tree
from visualizer.exporter import export_directory_structure
from pathlib import Path

@click.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False), required=True)
@click.option('--max-depth', default=-1, help='Maximum depth of the directory tree. Use -1 for unlimited depth.')
@click.option('--export', type=click.Choice(['ascii', 'matplotlib', 'networkx'], case_sensitive=False), 
              default='ascii', help='Format to export the directory structure. Default is ascii.')
@click.option('--output', type=click.Path(), help='Output file path to save the exported visualization. If not provided, defaults to ~/exports.')
def visualize(path, max_depth, export, output):
    """
    Visualize and export the directory structure starting from the specified PATH.
    """
    # Determine the export path
    if output is None:
        # Default export path if not specified
        output = str(Path.home() / "exports")
        click.echo(f"No output path provided, exporting to default directory: {output}")

    # Build the directory tree
    try:
        tree = build_tree(path, max_depth=max_depth)
    except Exception as e:
        click.echo(f"Error building the directory tree: {e}")
        return

    # Export the tree in the chosen format
    try:
        export_directory_structure(tree, export_format=export.lower(), output_path=output)
        click.echo(f"Directory structure exported successfully in {export} format to {output}.")
    except ValueError as e:
        click.echo(f"Error: {e}")
    except Exception as e:
        click.echo(f"An unexpected error occurred while exporting: {e}")

if __name__ == '__main__':
    visualize()
