from visualizer.export.ascii_exporter import export_to_ascii
from visualizer.export.matplotlib_exporter import export_to_matplotlib
from visualizer.export.networkx_exporter import export_to_networkx

import os
from pathlib import Path

def ensure_export_path(output_path):
    if output_path is None:
        # Default export path to the 'exports' directory in the user's home directory
        output_path = Path.home() / "exports"
    try:
        Path(output_path).mkdir(parents=True, exist_ok=True)
    except OSError as e:
        raise RuntimeError(f"Failed to create export directory at {output_path}: {e}")
    return output_path

def get_default_filename(export_format):
    # Default filenames based on the export format
    if export_format == 'ascii':
        return "directory_structure.txt"
    elif export_format == 'matplotlib' or export_format == 'networkx':
        return "directory_structure.png"
    else:
        return "directory_structure"

def export_directory_structure(tree, export_format='ascii', output_path=None):
    # Ensure the export path is valid and available
    output_dir = ensure_export_path(output_path)

    # Determine the filename if only a directory is provided
    if Path(output_dir).is_dir():
        output_file = Path(output_dir) / get_default_filename(export_format)
    else:
        output_file = Path(output_dir)

    # Export the tree in the specified format
    if export_format == 'ascii':
        export_to_ascii(tree, output_file)
    elif export_format == 'matplotlib':
        export_to_matplotlib(tree, output_file)
    elif export_format == 'networkx':
        export_to_networkx(tree, output_file)
    else:
        raise ValueError(f"Unsupported export format: {export_format}")

    print(f"Exported successfully to: {output_file}")
