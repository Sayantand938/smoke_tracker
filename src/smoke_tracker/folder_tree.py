# src/smoke_tracker/folder_tree.py

import os

def print_tree(directory, prefix="", exclude_dirs=None, script_name=None):
    if exclude_dirs is None:
        exclude_dirs = set()

    # Get sorted entries, filtering out hidden files
    entries = sorted(e for e in os.listdir(directory) if not e.startswith("."))
    
    for i, entry in enumerate(entries):
        full_path = os.path.join(directory, entry)

        # Skip excluded directories and its own script file
        if entry in exclude_dirs or (script_name and full_path == script_name):
            continue

        # Determine if this is the last entry
        is_last = i == len(entries) - 1
        connector = "└──" if is_last else "├──"
        print(f"{prefix}{connector} {entry}")

        # If it's a directory, recurse
        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            print_tree(full_path, prefix + extension, exclude_dirs, script_name)

if __name__ == "__main__":
    # Use the current working directory instead of assuming a fixed structure
    current_directory = os.getcwd()
    
    # Get the absolute path of this script to exclude it from printing
    script_name = os.path.abspath(__file__)

    print(f"Project Root Directory: {current_directory}")
    
    # Exclude common unnecessary directories
    exclude_dirs = {"node_modules", "venv", ".git", "__pycache__"}
    
    print_tree(current_directory, exclude_dirs=exclude_dirs, script_name=script_name)