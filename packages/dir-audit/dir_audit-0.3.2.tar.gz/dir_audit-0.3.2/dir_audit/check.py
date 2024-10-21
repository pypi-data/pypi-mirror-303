import os
from directory_tree import DisplayTree


def list_files_and_dirs(root_dir):
    for root, dirs, files in os.walk(root_dir):
        # Print the current directory path
        print(f"Directory: {root}")
        
        # Print all file paths in the current directory
        for file in files:
            file_path = os.path.join(root, file)
            print(f"File: {file_path}")
        
        # Print an empty line for better readability
        print()


def list_empty_dirs(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):        
        # Check if the current directory is empty
        if not os.listdir(root):
            print(f"Empty Directory: {root}")

            # Print an empty line for better readability
            print()


def list_files_and_dirs_with_substring(root_dir, substring):
    for root, dirs, files in os.walk(root_dir):
        # Check if the current directory name contains the substring
        if substring.lower() in os.path.basename(root).lower():
            print(f"Directory: {root}")
        
        # Filter and print file paths that contain the substring
        matching_files = [file for file in files if substring.lower() in file.lower()]
        for file in matching_files:
            file_path = os.path.join(root, file)
            print(f"File: {file_path}")
        
        # Print an empty line if we found any matching files or directories
        if substring.lower() in os.path.basename(root).lower() or matching_files:
            print()


def check_dir(args):
    print("Checking dir...")

    if args.empty:
        list_empty_dirs(args.path)

    if args.contains:
        list_files_and_dirs_with_substring(args.path, args.contains)

    if args.full:
        DisplayTree(args.path)
