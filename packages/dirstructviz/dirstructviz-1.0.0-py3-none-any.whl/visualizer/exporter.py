from visualizer.export.ascii_exporter import export_to_ascii
from visualizer.export.matplotlib_exporter import export_to_matplotlib
from visualizer.export.networkx_exporter import export_to_networkx

import os
from pathlib import Path

def ensure_export_path(output_path):
    if output_path is None:
        # Default export path to the 'exports' directory in the user's home directory
        output_path = Path.home() / "exports"
    Path(output_path).mkdir(parents=True, exist_ok=True)
    return output_path

def export_directory_structure(tree, export_format='ascii', output_path=None):
    output_path = ensure_export_path(output_path)

    if export_format == 'ascii':
        export_to_ascii(tree, output_path)
    elif export_format == 'matplotlib':
        export_to_matplotlib(tree, output_path)
    elif export_format == 'networkx':
        export_to_networkx(tree, output_path)
    else:
        raise ValueError(f"Unsupported export format: {export_format}")
