
"""Simple reporting library



"""
import os
import jinja2
import matplotlib.pyplot as plt


class Report(object):

    def __init__(self, output='./', figdir='fig', figfmt='.pdf'):
        self.text = []
        self.data = dict()
        self.output = output
        self.figdir = os.path.join(self.output, figdir)
        self.figfmt = figfmt

        # check directory
        if not os.path.exists(self.output):
            os.makedirs(os.path.join(self.output))

        if not os.path.exists(self.figdir):
            os.makedirs(self.figdir)

    def add_text(self, text):
        self.text.append(text)

    def add_data(self, **kvargs):
        self.data.update(kvargs)

    def add_fig(self, fig, figname):
        relpath = os.path.join(self.figdir, figname + self.figfmt)
        abspath = os.path.join(self.output, relpath)

        self.text.append("![figname]({})\n".format(relpath))
        fig.savefig(abspath)

    def generate(self, filename=None):
        text = ''.join(self.text)
        template = jinja2.Template(text)
        out = template.render(**self.data)

        if filename is not None:
            with open(os.path.join(self.output, filename), 'w') as f:
                f.write(out)

        return out

