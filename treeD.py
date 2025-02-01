import os
import argparse

def generate_tree(dir_path, prefix="", omit_dirs=set(), lines=None):
    """
    Recursively builds the tree structure of the directory.

    Parameters:
        dir_path (str): The directory to process.
        prefix (str): The string prefix for the current level (for drawing lines).
        omit_dirs (set): Set of directory names to omit from recursive listing.
        lines (list): List of strings representing the tree lines; if None, a new list is created.

    Returns:
        list: A list of strings representing the folder tree.
    """
    if lines is None:
        lines = []
    try:
        items = os.listdir(dir_path)
    except PermissionError:
        lines.append(prefix + "└── " + "[Permission Denied]")
        return lines

    # Sort directories first (alphabetically), then files.
    items = sorted(items, key=lambda x: (not os.path.isdir(os.path.join(dir_path, x)), x.lower()))
    count = len(items)

    for index, item in enumerate(items):
        item_path = os.path.join(dir_path, item)
        connector = "└── " if index == count - 1 else "├── "

        if os.path.isdir(item_path):
            lines.append(prefix + connector + item + "/")
            # If the directory is in the omit list, skip descending into it.
            if item in omit_dirs:
                continue
            new_prefix = prefix + ("    " if index == count - 1 else "│   ")
            generate_tree(item_path, new_prefix, omit_dirs, lines)
        else:
            lines.append(prefix + connector + item)
    return lines

def copy_to_clipboard(text):
    try:
        import pyperclip
        pyperclip.copy(text)
        print("\nFolder structure copied to clipboard.")
    except Exception as e:
        print("Error copying to clipboard:", e)



def main():
    parser = argparse.ArgumentParser(
        description="Display the folder structure as a tree. " +
                    "Standard directories (like .git and node_modules) are omitted by default. " +
                    "Use -o to specify additional folder names to omit and -c to copy the output to the clipboard."
    )
    parser.add_argument(
        "directory", nargs="?", default=".",
        help="Root directory to display (default: current directory)"
    )
    parser.add_argument(
        "-o", "--omit", nargs="*", default=[],
        help="Folder names to omit (do not list their content) when encountered."
    )
    parser.add_argument(
        "-c", "--clipboard", action="store_true",
        help="Copy the resulting folder structure to the clipboard."
    )
    args = parser.parse_args()

    # Define standard directories to always omit.
    default_omit_dirs = {'.git', 'node_modules'}

    # Combine default omitted directories with those provided by the user.
    omit_dirs = default_omit_dirs.union(set(args.omit))

    # Convert the root directory to an absolute path.
    root = os.path.abspath(args.directory)
    base = os.path.basename(root) if os.path.basename(root) else root

    # Build the tree structure as a list of lines.
    lines = [base + "/"]
    generate_tree(root, "", omit_dirs, lines)
    output = "\n".join(lines)

    # Print the tree.
    print(output)

    # Copy to clipboard if the -c flag is provided.
    if args.clipboard:
        copy_to_clipboard(output)

if __name__ == "__main__":
    main()
