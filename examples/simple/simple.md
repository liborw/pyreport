---
title: Example report
date: Monday 03. December 2018
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
<tr><td style="text-align: right;">0.843857</td><td style="text-align: right;">0.129319 </td><td style="text-align: right;">0.445584 </td><td style="text-align: right;">0.405611</td><td style="text-align: right;">0.29764 </td></tr>
<tr><td style="text-align: right;">0.177953</td><td style="text-align: right;">0.215457 </td><td style="text-align: right;">0.566621 </td><td style="text-align: right;">0.967487</td><td style="text-align: right;">0.194648</td></tr>
<tr><td style="text-align: right;">0.519841</td><td style="text-align: right;">0.464308 </td><td style="text-align: right;">0.0111792</td><td style="text-align: right;">0.161989</td><td style="text-align: right;">0.704424</td></tr>
<tr><td style="text-align: right;">0.422554</td><td style="text-align: right;">0.0595164</td><td style="text-align: right;">0.415479 </td><td style="text-align: right;">0.295931</td><td style="text-align: right;">0.785872</td></tr>
<tr><td style="text-align: right;">0.158049</td><td style="text-align: right;">0.717509 </td><td style="text-align: right;">0.64406  </td><td style="text-align: right;">0.474985</td><td style="text-align: right;">0.624561</td></tr>
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