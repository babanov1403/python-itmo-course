import os

__all__ = ['build_table', 'build_picture', 'save_string_as_tex']

def build_table(data: list[list], caption = "") -> str:
    if len(data) == 0:
        return ""
    if len(data[0]) == 0:
        return ""
    
    rows = len(data)
    columns = len(data[0])

    # validation 
    for lst in data:
        if len(lst) != columns:
            raise Exception("array of arrays is not a rectangle")

    tabular = ''.join(['|c'] * columns) + '|'

    transformed_data = [''] * rows
    for idx, lst in enumerate(data):
        transformed_data[idx] = ' & '.join(str(item) for item in lst) + R' \\ \hline'
    
    indent = " " * 8

    transformed_data = '\n'.join(f"{indent}{line}" for line in transformed_data)

    tex_code = \
fR"""\begin{{table}}
    \centering
    \begin{{tabular}}{{{tabular}}}
    \hline
{transformed_data}
    \end{{tabular}}
    \caption{{{caption}}}
\end{{table}}
    """
    return tex_code

def build_picture(path_to_png: str, caption: str = ""):
    tex_code = \
fR"""\begin{{figure}}
\centering
\includegraphics[width=0.25\linewidth]{{{path_to_png}}}
\caption{{{caption}}}
\end{{figure}}"""
    return tex_code

def save_string_as_tex(filename: str, string: str, path: str = "artefacts"):
    file = open(f"{os.path.join(path, filename)}.tex", "w")
    file.write(string)
    file.close()

def _test_build_table():
    tests = dict()

    tests['basic'] = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    tests['empty'] = [[]]
    tests['words'] = [['hello'], ['my'], ['name'], ['is']]
    tests['random'] = [['sorry', 'for', 'mat'], ['my', 80085, 'azamath'], [1.1, 1.2, 2.3]]

    tests['invalid'] = [[1, 2], [1], [1, 2]]

    for test_name, data in tests.items():
        result = str()
        try:
            result = build_table(data)
        except Exception as e:
            result = str(e)

        with open(f"artefacts/{test_name}.txt", "w") as file:
            file.write(str(data))

        save_string_as_tex(test_name, result)

def _test_build_picture():
    tests = ['frog', 'dog', 'chat_gpt']
    for png_name in tests:
        result = str()
        try:
            result = build_picture(os.path.join('pictures', png_name, '.png'))
        except Exception as e:
            result = str(e)
        save_string_as_tex(png_name, result)

if __name__ == "__main__":
    _test_build_table()
    _test_build_picture()

# понять как сделать свою библиотеку
# 