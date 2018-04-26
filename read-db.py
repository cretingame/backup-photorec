#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
import sqlite3
import time

start = time.time()

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
		#print(data)
		pass


end = time.time()

duration = end - start

print("Elaspsed time: {} seconds".format(duration))
