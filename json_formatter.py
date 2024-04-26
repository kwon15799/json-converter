import json

def parse_line(line):
    level = line.count('>')
    label = line.strip('>').strip()
    return level, label

def add_to_structure(structure, path, label):
    if not path:

        # 래이블
        structure.append({"title": label, "children": []})
        return structure[-1]
    
    else:
        return add_to_structure(structure[-1]["children"], path[1:], label)

def create_hierarchy_from_lines(lines):
    """Creates a hierarchical structure of dictionaries from lines of text."""
    root = []
    path = []
    last_level = -1
    
    for line in lines:
        level, label = parse_line(line)
        if level > last_level:

            # 한스텝더
            path.append(level)
        elif level < last_level:

            # 패스 바꾸자
            del path[last_level - level:]

        # Update
        node = add_to_structure(root if not path else root, path[:-1], label)
        last_level = level

    return root

def main(input_filename, output_filename):
    """Reads an indented text file, builds a hierarchical structure, and writes it as a JSON."""
    with open(input_filename, 'r') as file:

        # I will make it first read lines and make that down 
        lines = file.readlines()
    
    # 그 레벨 그대로 넣어
    hierarchy = create_hierarchy_from_lines(lines)
    
    with open(output_filename, 'w') as file:
        json.dump(hierarchy, file, indent=4)

##############################################################################################

main('input.txt', 'output.txt')
