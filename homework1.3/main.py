import sys

def input_lines():
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)
    return '\n'.join(content)

def get_stats(string):
    return string.count('\n'), len(string.split()), len(string)

def run():
    if len(sys.argv) == 1:
        content = '\n'.join(input_lines())
        lines, words, bytes = get_stats(content)
        print(f"{lines:8}{words:8}{bytes:8}")
        return
    
    for idx, file_name in enumerate(sys.argv[1:]):
        with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read()
                lines, words, bytes = get_stats(text)
                total_lines += lines
                total_words += words
                total_chars += bytes    
                print(f"{lines:8}{words:8}{bytes:8} {file_name}")

    if len(sys.argv) > 2:
        print(f"{total_lines:8}{total_words:8}{total_chars:8} total")

if __name__ == "__main__":
    run()

