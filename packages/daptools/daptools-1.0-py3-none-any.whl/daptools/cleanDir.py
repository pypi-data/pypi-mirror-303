#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
cleanDir
Clears files of following types: *.aux, *.log, *.gz produced by LaTeX.
Dir location is specified in __path__ 

Created on 18/05/2017, 13:14

@author: David Potucek
'''

import os

from myTools import treeWalker, getFileExtension

__koncovky__ = ('aux', 'log', 'gz')

__path__ = '/Users/david/Documents/work/O2/administrativa/TimeSheets/2018/'   #akceptaky
# __path__ = '/Users/david/Documents/work/O2/administrativa/nabidky/'     # nabidky


def filterFiles(soubory):
    output = []
    for name in soubory:
        for extension in __koncovky__:
            m, ext = getFileExtension(name)
            if extension == ext:
                output.append(name)
                break
    return output


if __name__ == "__main__":
    # os.chdir(os.path.dirname(__file__))   # zmena working dir na tu ze ktere jsme to spustili.
    # cesta = os.getcwd()
    # cesta = '/Users/david/temp'
    cesta = __path__
    print(cesta)
    files = treeWalker(cesta, False)
    keSmazani = filterFiles(files)
    print(keSmazani)
    for soubor in keSmazani:
        os.remove(soubor)
    print('{} files removed'.format(len(keSmazani)))

