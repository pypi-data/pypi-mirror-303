#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
LaTeXHelper - helper for generating LaTeX entities from Python.
Created on 19/10/2017, 08:47

@author: David Potucek
'''

def generateTableRow(*args):
    """Accepts arguments, makes them string and composes one row of LaTeX table."""
    row = []
    for arg in args:
        element = str(arg)
        row.append(element)
        row.append(' & ')
    row = row[:-1]
    vysledek = ''.join(row)
    return vysledek + ' \\\\'


if __name__ == "__main__":
    vys = generateTableRow('prvni', 'druhy', 'treti', 'ctvrty')
    print(vys)