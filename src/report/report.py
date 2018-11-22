"""Dead simple reporting library

This library provides simple way how to generate
arbitrary documents, 

"""

import jinja2
import logging

"""!
Reports are produces from multiline textbocks.

"""


class Report(object):

    def __init__(self):
        self.data = dict()

    def add_data(self, **kvargs):
        




        self.data.update(kvargs)

    def generate(self, ):
        text = ''.join(self.text)
        template = jinja2.Template(text)
        out = template.render(**self.data)

        return out


def parse_text_fields(s, start='"""!', end='"""'):

    lines = []
    isin = False
    for line in s.split('\n'):
        if line.startswith(start):
            isin = True
        elif line.startswith(end):
            isin = False
        elif isin:
            lines.append(line)
    return '\n'.join(lines)

