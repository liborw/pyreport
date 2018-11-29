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
<tr><td style="text-align: right;">0.174681</td><td style="text-align: right;">0.31114 </td><td style="text-align: right;">0.767087 </td><td style="text-align: right;">0.829891</td><td style="text-align: right;">0.855918 </td></tr>
<tr><td style="text-align: right;">0.644029</td><td style="text-align: right;">0.903491</td><td style="text-align: right;">0.987289 </td><td style="text-align: right;">0.434429</td><td style="text-align: right;">0.0223158</td></tr>
<tr><td style="text-align: right;">0.760308</td><td style="text-align: right;">0.412391</td><td style="text-align: right;">0.0959703</td><td style="text-align: right;">0.898275</td><td style="text-align: right;">0.650322 </td></tr>
<tr><td style="text-align: right;">0.646665</td><td style="text-align: right;">0.643411</td><td style="text-align: right;">0.829877 </td><td style="text-align: right;">0.345089</td><td style="text-align: right;">0.393184 </td></tr>
<tr><td style="text-align: right;">0.503216</td><td style="text-align: right;">0.774471</td><td style="text-align: right;">0.244256 </td><td style="text-align: right;">0.608441</td><td style="text-align: right;">0.991782 </td></tr>
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