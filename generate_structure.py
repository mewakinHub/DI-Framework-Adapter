import os

def create_structure_from_markdown(markdown_file):
    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip()
        if line.startswith('├──') or line.startswith('└──'):
            path = line[4:].strip()
            if path.endswith('/'):
                os.makedirs(path, exist_ok=True)
            else:
                dir_path = os.path.dirname(path)
                if dir_path:
                    os.makedirs(dir_path, exist_ok=True)
                with open(path, 'w') as fp:
                    pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_structure.py <path_to_markdown_file>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    create_structure_from_markdown(markdown_file)
    print(f"Structure created based on {markdown_file}")
