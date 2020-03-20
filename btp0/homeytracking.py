#!/usr/bin/python

import bluetooth
import time
import urllib2

print "In/Out Board"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    result = bluetooth.lookup_name('3C:28:6D:FB:80:C0', timeout=5)
    if (result != None):
        print "P3XL: in"
        #urllib2.urlopen("http://192.168.178.XXX/api/app/com.internet/presence/home").read()
    else:
        print "P3XL: out"
        #urllib2.urlopen("http://192.168.178.XXX/api/app/com.internet/presence/away").read()
    print "Sleeping for 5"
    time.sleep(5)


'''
SOURCE: https://gist.github.com/DieterKoblenz/15415aadf37dfbca2ac11759de32040c/raw/ea21233cb0fbd6f8c3b3889b5deee5644bba4931/homeytracking.py
https://forum.athom.com/discussion/1975/how-to-presence-detection-using-a-raspberry-pi-3-and-a-bluetooth-phone-tag
'''
