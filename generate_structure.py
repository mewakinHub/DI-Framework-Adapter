import os
import sys

def create_structure_from_markdown(markdown_file):
    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip()
        if line.startswith('├──') or line.startswith('└──'):
            path = line[4:].strip()
            if path.endswith('/'):
                try:
                    os.makedirs(path, exist_ok=True)
                    print(f"Directory created: {path}")
                except Exception as e:
                    print(f"Error creating directory {path}: {e}")
            else:
                dir_path = os.path.dirname(path)
                if dir_path:
                    try:
                        os.makedirs(dir_path, exist_ok=True)
                        print(f"Directory created: {dir_path}")
                    except Exception as e:
                        print(f"Error creating directory {dir_path}: {e}")
                try:
                    with open(path, 'w') as fp:
                        pass
                    print(f"File created: {path}")
                except Exception as e:
                    print(f"Error creating file {path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_structure.py <path_to_markdown_file>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    create_structure_from_markdown(markdown_file)
    print(f"Structure created based on {markdown_file}")
