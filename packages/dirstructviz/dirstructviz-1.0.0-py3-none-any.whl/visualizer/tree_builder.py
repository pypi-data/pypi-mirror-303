from pathlib import Path

class TreeNode:
    def __init__(self, name, is_dir):
        self.name = name
        self.is_dir = is_dir
        self.children = []

def build_tree(path, max_depth=-1, current_depth=0):
    path = Path(path)
    node = TreeNode(path.name, path.is_dir())
    if path.is_dir() and (max_depth == -1 or current_depth < max_depth):
        for child in path.iterdir():
            node.children.append(build_tree(child, max_depth, current_depth + 1))
    return node
