#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Generuje nahodne passwords pro inet sites.
Created on 13.04.2020

@author: David Potucek x david
'''

import random
__CHAR__ ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
__NUM__ = '1234567890'
__SPECI__= '!@#$%^&*()_+}{'
__LEN__ = 16
__MIX__ = '012'


def generatePaaswd(length):
    mix = 0
    password = ""
    for i in range(length + 1):
        if mix == '0':
            password += random.choice(__CHAR__)
        if mix == '1':
            password += random.choice(__NUM__)
        if mix == '2':
            password += random.choice(__SPECI__)
        mix = random.choice(__MIX__)
    return password


if __name__ == "__main__":
    password = ""
    key = input('pro passwd zmackni neco, pro konec zmackni q\n')
    while (key != 'q'):
        password = generatePaaswd(__LEN__)
        print(password)
        password = ''
        key = input('pro passwd zmackni neco, pro konec zmackni q')
