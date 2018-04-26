#!/usr/bin/env python

# -*- coding: utf-8 -*-

from lxml import etree
import sqlite3

conn = sqlite3.connect('report.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE files
             (rowid INTEGER PRIMARY KEY AUTOINCREMENT, filename text, size integer)''')
#c.execute('''CREATE TABLE IF NOT EXISTS files
#             (rowid INTEGER PRIMARY KEY AUTOINCREMENT, filename text, size integer)''')

tree = etree.parse("report.xml")
root = tree.getroot()

print("tree loaded ...")

for fileobject in root.iter('fileobject'):
	filename = fileobject.find('filename').text
	filesize = fileobject.find('filesize').text
	#byte_runs = fileobject.find('byte_runs')
	#byte_run = byte_runs.find('byte_run')
	#offset = byte_run.get('offset')
	#img_offset = byte_run.get('img_offset')
	#length = byte_run.get('len')
	#print("{} {}".format(filename,filesize))
	c.execute("INSERT INTO files(filename,size) VALUES ('{}',{})".format(filename,filesize))

print("xml file read")

conn.commit()

print("changes commited to the DB")

conn.close()
