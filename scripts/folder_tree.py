import os
import fnmatch

def print_tree(directory, prefix="", exclude_dirs=None, exclude_patterns=None):
    if exclude_dirs is None:
        exclude_dirs = set()

    if exclude_patterns is None:
        exclude_patterns = set()

    # Get sorted entries, filtering out hidden files
    entries = sorted(e for e in os.listdir(directory) if not e.startswith("."))

    for i, entry in enumerate(entries):
        full_path = os.path.join(directory, entry)

        # Skip excluded directories and patterns
        if entry in exclude_dirs or any(fnmatch.fnmatch(entry, pattern) for pattern in exclude_patterns):
            continue

        # Determine if this is the last entry
        is_last = i == len(entries) - 1
        connector = "└──" if is_last else "├──"
        print(f"{prefix}{connector} {entry}")

        # If it's a directory, recurse
        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            print_tree(full_path, prefix + extension, exclude_dirs, exclude_patterns)

if __name__ == "__main__":
    # Use the current working directory instead of assuming a fixed structure
    current_directory = os.getcwd()

    print(f"Project Root Directory: {current_directory}")

    # Exclude common unnecessary directories
    exclude_dirs = {"node_modules", "venv", ".git", "__pycache__", "build", "dist"}

    # Exclude patterns
    exclude_patterns = {"*.egg-info"}

    print_tree(current_directory, exclude_dirs=exclude_dirs, exclude_patterns=exclude_patterns)
