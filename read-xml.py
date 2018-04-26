#!/usr/bin/env python

# -*- coding: utf-8 -*-

from lxml import etree
import sys
import time

start = time.time()

print("Loading tree ...")

tree = etree.parse("report.xml")
root = tree.getroot()

print("Tree loaded")

i=0
for fileobject in root.iter('fileobject'):
	filename = fileobject.find('filename').text
	filesize = fileobject.find('filesize').text
	#i=i+1
	#sys.stdout.write("{} files read\r".format(i))

end = time.time()

duration = end - start

print("Elaspsed time: {} seconds".format(duration))
