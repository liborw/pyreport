#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage:
    report1.py [options] [<output>]

Options:
    -v VAL, --value VAL         Value to be placed in the report.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from docopt import docopt
from report import Report
from tabulate import tabulate

## malual parametrs {{{

opt = dict()
opt['value'] = '42'

# }}}
## commad line parametrs {{{

opt = docopt(__doc__)


# }}}
## start report {{{

report = Report()

"""
# A dummy report

This is a dummy report. This is a demonstration of the inline
value {{ inline }}.

{% if opt.value %}
Also command line arguments can be passed to the report
like this one: {{ opt.value }}.
{% endif %}

"""
report.add_text(_)
report.add_data(inline=10, opt=opt)

# }}}
## tables {{{

"""
Table
-----

In this section we will show table:

{{ table }}


"""
report.add_text(_)
rand = np.random.rand(5,5)
table = tabulate(rand, range(5), tablefmt='pipe')
report.add_data(table=table)

# }}}
## Figure {{{

"""
Figure
------

This is figure:

"""
report.add_text(_)


x = np.linspace(0, 6, 100)
y = np.sin(x)

fig = plt.figure()
plt.plot(x, y)

report.add_fig(fig, 'sinxy')



# }}}
## Generate output {{{

txt = report.generate('report.md')
print(txt)

# }}}
