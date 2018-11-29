
import numpy as np
import matplotlib.pyplot as plt
from pyreport.report import Report
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

<div style="align: center">
{{ table }}
</div>

"""

rand = np.random.rand(5, 5)
table = tabulate(rand, tablefmt='html')
report['table'] = table

"""!
## Figure

![Test image]({{ fig1 }})

"""

x = np.linspace(0, 6, 100)
y = np.sin(x)

fig = plt.figure()
plt.plot(x, y)

fig.savefig(report.add_path('fig/fig.png', 'fig1'))


"""!
----
This report was generated using [pyreports]().

"""

md = report.generate()
with open('example.md', 'w') as f:
    f.write(md)

html = markdown.markdown(md)
with open('example.html', 'w') as f:
    f.write(html)

weasyprint.HTML(string=html,base_url='./').write_pdf('example.pdf')


