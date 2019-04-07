#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
import sqlite3
import time
import re
from operator import itemgetter
import os

output_dir="/mnt/Restore/backups.sorted/"

start = time.time()


print("Loading db ...")
conn = sqlite3.connect('report.db')
c = conn.cursor()

c.execute('''SELECT * FROM files''')

end = False
ext_to_move = ["png","jpg","gif","mp3","pdf","doc","bmp","avi","wmf","ogg","wav","flac","vsdx","xls","csv","vsd","odt","docx","mkv","wmv","xlsx","wma","pptx","mov","7z","ogv","flv","3gp","kdb","epub","iso"]

selected_files = []

print("Db loaded ...")

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


		if( ext in ext_to_move) :
			new_filepath = re.sub(r'backups',r'backups.sorted/{}'.format(ext),filepath)
			if os.path.isfile(filepath):
				m = re.search(r'.*\/',new_filepath)
				new_dirpath = m.group(0)
				if not os.path.isdir(new_dirpath):
					os.mkdir(new_dirpath)
				os.rename(filepath,new_filepath)
				#print(new_dirpath)
				print("{} {}".format(filepath,new_filepath))
			elif os.path.isfile(new_filepath):
				print("{} already moved".format(new_filepath))
			else:
				print("{} ERROR".format(new_filepath))



end = time.time()

duration = end - start

print("{} files selected".format(len(selected_files)))
print("Elaspsed time: {} seconds".format(duration))

