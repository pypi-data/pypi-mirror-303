#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
testFile file pro testing kusu kodu
Created on 22/05/2017, 12:44

@author: David Potucek
'''

import zipfile

__DICT_PATH__ = '/usr/share/dict/web2'


if __name__ == "__main__":
    with zipfile.ZipFile('/Users/david/demo.zip', 'r') as archive:
        archive.printdir()
        first = archive.infolist()[0]
        with archive.open(first) as member:
            text = member.read()
            print(text)