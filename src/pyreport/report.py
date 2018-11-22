"""Dead simple reporting library

This library provides simple way how to generate
arbitrary documents, 

"""

import jinja2
import logging
import sys

log = logging.getLogger('report')


def parse_text_fields(s, start='"""!', end='"""'):

    lines = []
    isin = False
    for i, line in enumerate(s.split('\n')):
        if line.startswith(start):
            isin = True
            log.debug('Text block start at %d', i+1)
        elif line.startswith(end):
            isin = False
            log.debug('Text block end at %d', i+1)
        elif isin:
            lines.append(line)
    return '\n'.join(lines)


def report(**kvargs):
    src = sys.argv[0]
    log.debug('Source file: ', src)

    # read the whole file
    with open(src, 'r') as f:
        txt = f.read()

    # filter text blocks
    txt = parse_text_fields(txt)

    # prepare template
    tpl = jinja2.Template(txt)

    # render template
    out = tpl.render(**kvargs)
    return out




    
    



