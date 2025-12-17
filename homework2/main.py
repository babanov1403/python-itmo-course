import babanovtex_internal as bt
import babanovtex_external as bt_ext

import latex

def homework_2_1():
    # using bt.build_table
    data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    tex_table = bt.build_table(data)

    bt.save_string_as_tex("rofl_table", tex_table)

def get_valid(tex):
    return fR"""
\documentclass{{article}}
\usepackage{{graphicx}}
\begin{{document}}
{tex}
\end{{document}}
"""

def homework_2_2():
    data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    tex_table = bt_ext.build_table(data)

    pic = "/home/babanov1403/Desktop/ITMO/python/homework2/pictures/chat_gpt.png"
    tex_pic = bt_ext.build_picture(pic)

    tex = tex_table + '\n' + tex_pic

    tex = get_valid(tex)

    bt_ext.save_string_as_tex("homework2_2", tex)
    
    pdf = latex.build_pdf(tex)
    pdf.save_to('artefacts/homework2_2.pdf')

if __name__ == "__main__":
    homework_2_1()
    homework_2_2()
