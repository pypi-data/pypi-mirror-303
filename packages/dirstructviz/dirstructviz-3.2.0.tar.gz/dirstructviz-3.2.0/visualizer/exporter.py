from visualizer.export.ascii_exporter import export_to_ascii
from visualizer.export.matplotlib_exporter import export_to_matplotlib
from visualizer.export.networkx_exporter import export_to_networkx

def export_directory_structure(tree, export_format, output_path=None):
    """
    Export the directory structure to the specified format.

    :param tree: The directory tree to export.
    :param export_format: The format to export to ('ascii', 'matplotlib', 'networkx').
    :param output_path: Optional path to save the exported file.
    """
    if export_format == 'ascii':
        export_to_ascii(tree, output_path)
    elif export_format == 'matplotlib':
        export_to_matplotlib(tree, output_path)
    elif export_format == 'networkx':
        export_to_networkx(tree, output_path)
    else:
        raise ValueError(f"Unsupported export format: {export_format}")
