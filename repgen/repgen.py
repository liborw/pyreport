"""Dead simple reporting library

This library provides simple way how to generate
arbitrary documents, 

"""

import jinja2
import logging
import sys
import os

log = logging.getLogger('report')

confs = dict()
confs['default'] = {"text_block_start":     ['r"""!'],
                    "text_block_end":       ['"""'],
                    "jinja_block_start":    '{%',
                    "jinja_block_end":      '%}',
                    "jinja_varialbe_start": '{{',
                    "jinja_varialbe_end":   '}}',
                    "jinja_comment_start":  '{#',
                    "jinja_comment_end":    '#}',
                    "jinja_line_statement": None,
                    "jinja_line_comment":   None,
                    "jinja_trim_blocks":    True,
                    "jinja_autoescape":     False}

confs['latex'] = {"text_block_start":     ['"""!', 'r"""!'],
                  "text_block_end":       ['"""'],
                  "jinja_block_start":    '\BLOCK{',
                  "jinja_block_end":      '}',
                  "jinja_varialbe_start": '\VAR{',
                  "jinja_varialbe_end":   '}',
                  "jinja_comment_start":  '\#{',
                  "jinja_comment_end":    '}',
                  "jinja_line_statement": '%%',
                  "jinja_line_comment":   '%#',
                  "jinja_trim_blocks":    True,
                  "jinja_autoescape":     False}


def parse_text_fields(s, start=['"""!', 'r"""!'], end=['"""']):

    lines = []
    isin = False
    for i, line in enumerate(s.split('\n')):
        if startswithany(line, start):
            isin = True
            log.debug('Text block start at %d', i+1)
        elif startswithany(line, end):
            isin = False
            log.debug('Text block end at %d', i+1)
        elif isin:
            lines.append(line)
    return '\n'.join(lines)


def startswithany(s, tpl):
    for t in tpl:
        if s.startswith(t):
            return True
    else:
        return False


def get_config(name):
    if isinstance(name, (str,)):
        conf = confs[name]
    else:
        conf = name
    return conf


def generate(text=None, data={}, conf='default'):
    src = sys.argv[0]
    log.debug('Source file: ', src)

    # get config
    conf = get_config(conf)

    # read the whole file
    if text is None:
        with open(src, 'r') as f:
            content = f.read()

        # filter text blocks
        text = parse_text_fields(content, start=conf['text_block_start'], end=conf['text_block_end'])

    # prepare template
    env = jinja2.Environment(block_start_string = conf['jinja_block_start'],
                             block_end_string = conf['jinja_block_end'],
                             variable_start_string = conf['jinja_varialbe_start'],
                             variable_end_string = conf['jinja_varialbe_end'],
                             comment_start_string = conf['jinja_comment_start'],
                             comment_end_string = conf['jinja_comment_end'],
                             line_statement_prefix = conf.get('jinja_line_statement', None),
                             line_comment_prefix = conf.get('jinja_line_comment', None),
                             trim_blocks = conf.get('jinja_trim_blocks', True),
                             autoescape = conf.get('jinja_autoescape', False))

    tpl = env.from_string(text)

    # render template
    out = tpl.render(**data)
    return out


class Report(dict):

    def __init__(self, outdir='.', conf='default'):
        super(Report, self).__init__()
        self.outdir = outdir
        self.conf = get_config(conf)

    def add_data(self, **kvargs):
        """Add data as key value pairs."""
        self.update(kvargs)

    def add_path(self, filename, key=None):
        """
        Add relative path, key is the key used in text,
        returns path wher the figure should be saved.
        """

        # create missing subdirectory
        subdir = os.path.dirname(filename)
        path = os.path.join(self.outdir, subdir)
        if not os.path.isdir(path):
            os.makedirs(path)

        path = os.path.join(self.outdir, filename)
        log.debug('save path: %s for key %s', path, key)

        if key is not None:
            self[key] = filename

        return path

    def generate(self, text=None, data={}):
        """Parse text section and generate the report."""
        self.add_data(**data)
        out = generate(text=text, data=self, conf=self.conf)
        return out

