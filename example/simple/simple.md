---
title: Example report
date: Thursday 29. November 2018
---

# Example report

This is example report, showing how to include text, tables, figures and inline
values.

## Features

 - What do you get when you multiply six by nine? 42. (inline value)
 - Math: $`\delta = 1`$ (not really related to the pyreport library)
 - Tables
 - Plots

## Table

The following table is generated using [tabulate](https://pypi.org/project/tabulate/) library.
I'm using the html format as the github format desn't work in gitlab, and html works in both.

<div style="align: center">
<table>
<tbody>
<tr><td style="text-align: right;">0.592862</td><td style="text-align: right;">0.562464</td><td style="text-align: right;">0.303685 </td><td style="text-align: right;">0.00297459</td><td style="text-align: right;">0.768117</td></tr>
<tr><td style="text-align: right;">0.744525</td><td style="text-align: right;">0.118402</td><td style="text-align: right;">0.666833 </td><td style="text-align: right;">0.756358  </td><td style="text-align: right;">0.886459</td></tr>
<tr><td style="text-align: right;">0.808759</td><td style="text-align: right;">0.7703  </td><td style="text-align: right;">0.0964539</td><td style="text-align: right;">0.66587   </td><td style="text-align: right;">0.674644</td></tr>
<tr><td style="text-align: right;">0.633492</td><td style="text-align: right;">0.338505</td><td style="text-align: right;">0.258428 </td><td style="text-align: right;">0.893039  </td><td style="text-align: right;">0.377222</td></tr>
<tr><td style="text-align: right;">0.67076 </td><td style="text-align: right;">0.774994</td><td style="text-align: right;">0.784219 </td><td style="text-align: right;">0.297287  </td><td style="text-align: right;">0.731343</td></tr>
</tbody>
</table>
</div>

## Figure

The following figure is produced by [matplotlib](https://matplotlib.org), using the `Report.add_path('fig/fig.png')`
the figure is save to apropriate location.

![Test image](fig/fig.png)


Don't wat to force you, but it would be nice to mention the pyreport library, somewhere in the report.

----
This report was generated using [pyreport](https://github.com/liborw/pyreport).