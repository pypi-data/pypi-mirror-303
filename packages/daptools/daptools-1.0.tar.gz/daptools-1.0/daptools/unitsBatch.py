#!/usr/bin/python
# -*- coding: utf-8 -*-
"""converts inches in textual representation to millimeters.
Works even with inches in fraction.
Allows batch conversion:
input: text file input.txt with one number on line
output: text file output.txt with two numbers on line; first in, second mm.
"""

import csv

__DEBUG = True
__inFile = "input.txt"
__outFile = "output.txt"


def parseFraction(fraction):
    """ evaluates provided fraction to decadic number """
    if not checkFractionValidity(fraction):
        print("Error in fraction value, aborting")
        return 0
    delimiter = fraction.find('/')
    nominator = float(fraction[0:delimiter])
    denominator = float(fraction[delimiter + 1:])
    return nominator / denominator


def checkFractionValidity(fraction):
    first = fraction.find('/')  # check for double /
    rest = fraction[first + 1:]
    if rest.find('/') != -1:
        return False
    return True


def parseNumber(line):
    value = 0
    try:
        if line.find('/') >= 0:
            value = parseFraction(line)
        else:
            value = float(line)
        return value
    except ValueError:
        print("Invalid number %s" % (line))


def parse_csv(line):
    reader = csv.reader([line], delimiter=',')
    return reader.next()


def readFile():
    """Reads from input file comma delimited strings and converts to values.
    Returns list of rows containing float values"""
    numbers = []
    for line in open(__inFile):
        if (line.startswith('#') or line.startswith('\n')):
            continue
        else:
            fields = parse_csv(line)
            row = []
            for value in fields:
                number = parseNumber(value)
                row.append(number)
            numbers.append(row)
    return numbers


def processConvert(values):
    f = open(__outFile, 'w')
    for row in values:
        outRow = []
        from myTools import convertIn2Mm
        for strVal in row:
            val = str(convertIn2Mm(strVal))
            outRow.append(val)
        f.write(str(outRow))
        f.write('\n')
        if __DEBUG: print(outRow)
    f.flush()


if __name__ == "__main__":
    values = readFile()  # reads input file and returns list of string lists
    print("file input.txt read")
    for row in values:
        print(row)
    processConvert(values)  # converts and writes to the output file
    print("file output.txt written")


