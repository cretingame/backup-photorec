#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
import sqlite3
import time
import re
from operator import itemgetter

start = time.time()

counters = {}

print("Loading db ...")
conn = sqlite3.connect('report.db')
c = conn.cursor()

c.execute('''SELECT * FROM files''')

end = False

while end == False:
	data = c.fetchone()

	if data == None:
		end = True
	else:
		rowid = data[0]
		filepath = data[1]
		filesize = data[2]
		filename = re.sub(r'.*\/','',filepath)
		ext = re.sub(r'.*\.','',filename)

		
		if( ext == filename ):
			ext = 'no_ext'

		if ext in counters:
			counters[ext] = counters[ext] + 1
		else:
			counters[ext] = 1
		#print("{} {}".format(rowid,ext))

counterlist = sorted(counters.items(), key=itemgetter(1))

for counter in counterlist:
	print("{}: \t {}".format(counter[0],counter[1]))

end = time.time()

duration = end - start

print("Elaspsed time: {} seconds".format(duration))
