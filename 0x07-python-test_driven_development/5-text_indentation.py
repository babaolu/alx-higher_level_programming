#!/usr/bin/python3
"""
This module implements a function that indents texts
"""


def text_indentation(text=''):
    """ Add 2 newlines after . ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    for i in ".?:":
        text = text.replace(i, i + "\n\n")
    for line in text.splitlines():
        text = text.replace(line, line.strip())
    print(text, end="")
