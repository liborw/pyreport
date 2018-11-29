
import numpy as np
import matplotlib.pyplot as plt
from pyreport import Report
from tabulate import tabulate
from datetime import date
import markdown
import weasyprint

"""!
---
title: Example report
date: {{ date }}
---

# Example report

This is example report, showing how to include text, tables, figures and inline
values.

## Features

 - What do you get when you multiply six by nine? {{ value }}. (inline value)
 - Math: $`\delta = 1`$ (not really related to the pyreport library)
 - Tables
 - Plots

"""

report = Report()
report['value'] = 42
report['date'] = date.today().strftime("%A %d. %B %Y")

"""!
## Table

The following table is generated using [tabulate](https://pypi.org/project/tabulate/) library.
I'm using the html format as the github format desn't work in gitlab, and html works in both.

<div style="align: center">
{{ table }}
</div>

"""

rand = np.random.rand(5, 5)
table = tabulate(rand, tablefmt='html')
report['table'] = table

"""!
## Figure

The following figure is produced by [matplotlib](https://matplotlib.org), using the `Report.add_path('fig/fig.png')`
the figure is save to apropriate location.

![Test image]({{ fig1 }})

"""

x = np.linspace(0, 6, 100)
y = np.sin(x)

fig = plt.figure()
plt.plot(x, y)

fig.savefig(report.add_path('fig/fig.png', 'fig1'))


"""!

Don't wat to force you, but it would be nice to mention the pyreport library, somewhere in the report.

----
This report was generated using [pyreport](https://github.com/liborw/pyreport).

"""

md = report.generate()
with open('simple.md', 'w') as f:
    f.write(md)

html = markdown.markdown(md)
with open('simple.html', 'w') as f:
    f.write(html)

weasyprint.HTML(string=html,base_url='./').write_pdf('simple.pdf')


