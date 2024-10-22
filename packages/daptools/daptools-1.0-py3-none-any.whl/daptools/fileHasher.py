#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
fileHasher - vezme files z adresare (bez subdirs) a prejmenuje je tak, aby 
zacinaly v nahodnem poradi - predradi jim 3 cisla a prida pomlcku. 
Napr. 0007-oldFileName.xyz.
Pouzivam pro muziku.
Created on 27/04/2017, 07:26

@author: David Potucek
"""

import random

from myTools import treeWalker, separateFullPath, renameFiles, prepareCounter, stripCzechChars

__PATH = '/Users/david/temp/mp3'
__IGNORE_NAMES__ = ('.DS_Store')    # ktere files vynechat
__REPLACE_CHARS__ = ('.', ' ', '-', '_') # ktere znaky vynechat na zacatku filename

def stripFirstAlphanumeric(fileName, position=6):
    """odstrani z prvnich x znaku cisla a to co je v __REPLACE_CHARS__
    Funguje pouze na soubory s priponou, ty bez pripony zastavi cely program
    :param fileName name
    :param position - kolik znaku na zacatku prohledavat
    :return  nove jmeno"""
    import sys
    fileName = stripCzechChars(fileName)
    try:
        index = fileName.rindex('.')    # najdu priponu
    except ValueError:
        print("ERROR: invalid filename, no extension found!")
        sys.exit(1)         # zastavujeme, pres validace proslo neco co nemelo!
    ext = fileName[index:]
    fileName = fileName[:index]
    nameStr = fileName[:position]
    restStr = fileName[position:]
    result = ''.join(i for i in nameStr if not (i.isdigit() or i in __REPLACE_CHARS__))
    result = result + restStr + ext
    return result

def hashNames(fNames, randomize = 0):
    '''k danemu seznamu files vyrobi dictionary se starym a novym filename
    serazene nahodne.
    :param fNames name tuple (full path)
    :param randomize switch 0 means randomize, anything else - no change of order
    :return dictionary of old and new file names (full path)'''
    counter = 1
    l = list(fNames)
    newNames = {}

    directoryPath = validateFiles(l)

    while len(l) > 0:       # samotna funkce zpracovani file name
        if randomize == 0:
            element = random.choice(l)
        else:
            element = l[counter]
        path, name = separateFullPath(element)
        nameR = stripFirstAlphanumeric(name)
        nameNew = directoryPath + prepareCounter(counter) + '-' + nameR
        newNames[element] = nameNew
        l.remove(element)
        counter += 1
    return newNames

def removeNumbersFromFiles(fNames):
    ''' Projde dodany list souboru, zvaliduje jejich jmena a vyjme numericke znaky na
    jejich zacatku.
    :param fNames file names tuple (full path)
    :return dictionary of old and new file names (full path)
    '''
    l = list(fNames)
    newNames = {}

    directoryPath = validateFiles(l)
    while len(l) > 0:
        element = l[0]
        path, name = separateFullPath(element)
        nameStrip = stripFirstAlphanumeric(name)
        nameNew = directoryPath + nameStrip
        newNames[element] = nameNew
        l.remove(element)
    return newNames


def validateFiles(l):
    '''Rutina zkontroluje jestli soubor ma priponu a jestli neni v ignorovanych.
    :return directoryPath je full path k danym souborum
    Pozor! modifikuje list l bez toho aby ho vracel!'''
    for nam in l:
        dir, n = separateFullPath(nam)
        try:
            index = n.rindex('.')  # najdu priponu
        except ValueError:        # if nema priponu, vyhodim ho
            l.remove(nam)
            continue
        if n in __IGNORE_NAMES__:   # if je v ignorovanych files, vyhodim ho
            l.remove(nam)
    print('z toho {} platnych'.format(len(l)))
    directoryPath, name = separateFullPath(l[0])  # pripravim si path
    return directoryPath


if __name__ == "__main__":
    l = treeWalker(__PATH, False)
    print('nacteno {} files.'.format(len(l)))
    newNames = removeNumbersFromFiles(l)        # tohle odstrani ciselne prefixy
    newNames = hashNames(l)                   # tohle zahashuje soubory podle cisel
    # print(newNames)
    renameFiles(newNames)
    print('Done!')



