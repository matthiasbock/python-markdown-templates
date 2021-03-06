#!/usr/bin/python3

from IPython.display import display, Markdown
from string import Template

#
# Opens a Markdown formatted file
# and replaces all $variables with
# values from itself
#
class MarkdownTemplate():
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        f = open(self.filename, "r")
        s = f.read()
        f.close()
        t = Template(s)
        s = t.substitute(self.__dict__)
        return s

    def show(self):
        display(Markdown(str(self)))
