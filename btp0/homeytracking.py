#!/usr/bin/python

import bluetooth
import time
import urllib2
import yaml
import sys

print "In/Out Board"

inRange = False
interval = 2

if (sys.argv != ""):
    config = yaml.safe_load(open(sys.argv))

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    result = bluetooth.lookup_name('3C:28:6D:FB:80:C0', timeout=5)
    if (result != None):
        print "P3XL: in"
    else:
        print "P3XL: out"
    if (inRange != (result != None)): # check for a state change, you dont want to DOS ifttt
        inRange = (result != None)
        print "new state: " + str(inRange)
    print "Sleeping for " + str(interval)
    time.sleep(interval)


'''
SOURCE: https://gist.github.com/DieterKoblenz/15415aadf37dfbca2ac11759de32040c/raw/ea21233cb0fbd6f8c3b3889b5deee5644bba4931/homeytracking.py
https://forum.athom.com/discussion/1975/how-to-presence-detection-using-a-raspberry-pi-3-and-a-bluetooth-phone-tag
'''
