---
title:  Developement Notes for RepGen
author: Libor Wagner <libor.wagner@cvut.cz>
date:   2018-12-04
---

# Developement Notes for RepGen

These are my developement notes for the RepGen library.

## PyPi package

 - build package: `python3 setup.py sdist bdist_wheel`
 - upload package: `twine upload dist/*`
 - More in [Tutorial: Packaging Projects](https://packaging.python.org/tutorials/packaging-projects/)

## Useful libraries

 - [bokeh](https://bokeh.pydata.org/en/latest/), html integration works fine but didn't found easy way to integrate it inside markdown (gitlab/github)
 - [weasyprint](https://weasyprint.org/), from html to pdf

## Misc notes

 - PyPi doesn't know front matter...

## Improvement ideas

 - ...
 - Language specific extensions
