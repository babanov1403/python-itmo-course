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
    content = []
    if len(file_name) == 0:
        content = input_lines()
    else:
        with open(file_name, 'r') as file:
                content = file.read().split('\n')

    content = [line.strip() for line in content]
    while len(content) > 0 and len(content[-1]) == 0:
        content.pop()
    max_width = len(str(len(content)))
    idx = 0
    for line in content:
        if len(line.strip()) == 0:
            print()
        else:
            print(f'{idx + 1:>{max_width + 4}} ', line)
            idx += 1

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            run(sys.argv[1])
        else:
            run("")
    except:
        print("Oops... Some error babanov")