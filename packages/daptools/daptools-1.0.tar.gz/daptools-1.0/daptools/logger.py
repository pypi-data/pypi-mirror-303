#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
logger - writes simple pair of time, event to the file
Created on 18/05/2017, 14:29

@author: David Potucek
'''


class DataLoger():

    def __init__(self, file):
        self.soubor = file

    def writeEvent(self, event):
        with open(self.soubor, mode="a", encoding="utf8") as fileHandler:
            fileHandler.write(event + '\n')
        fileHandler.close()
        return



if __name__ == "__main__":
    f = '/Users/david/temp/logger.txt'      # example usage
    import datetime, time
    now = datetime.datetime.now().ctime()
    loger = DataLoger(f)
    muster = "Událost číslo: "
    counter = 1
    while counter <=10:
        event = now + ' ' + muster + str(counter)
        loger.writeEvent(event)
        print('zapsano do souboru, counter = {}.'.format(counter))
        counter += 1
        time.sleep(1)
    print('Done!')