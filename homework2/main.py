import sys

def input_lines():
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)
    return content

def run(file_name: str):
    if len(file_name) == 0:
        content = input_lines()
        content = [line.strip() for line in content]
        while len(content) > 0 and len(content[-1]) == 0:
            content.pop()

        for line in content[-17:]:
            if len(line.strip()) == 0:
                print()
            else:
                print(line)
        return

    with open(file_name, 'r') as file:
        content = file.read().split('\n')
        content = [line.strip() for line in content]
        while len(content) > 0 and len(content[-1]) == 0:
            content.pop()

        for line in content[-10:]:
            if len(line.strip()) == 0:
                print()
            else:
                print(line)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run("")