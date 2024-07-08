import os

def create_structure_from_markdown(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_path = []
    for line in lines:
        if line.startswith('#'):
            level = line.count('#')
            title = line.strip('#').strip().replace(' ', '_').lower()
            if '.' in title:
                # It's a file
                path = os.path.join(*current_path[:level-1])
                file_path = os.path.join(path, title)
                os.makedirs(path, exist_ok=True)
                with open(file_path, 'w') as f:
                    f.write('')
                print(f"File created: {file_path}")
            else:
                # It's a directory
                current_path = current_path[:level-1]
                current_path.append(title)
                os.makedirs(os.path.join(*current_path), exist_ok=True)
                print(f"Directory created: {os.path.join(*current_path)}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python create_structure.py <path_to_markdown_file>")
        sys.exit(1)

    md_file = sys.argv[1]
    create_structure_from_markdown(md_file)
    print(f"Structure created based on {md_file}")
