import sys

def run(file_name: str):
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
        run(sys.argv[1])
    except:
        print("Oops... Some error babanov")