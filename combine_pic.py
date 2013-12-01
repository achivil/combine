#! -*-coding: utf-8-*-

import os
import shutil

picfile = ['jpg', 'jpeg', 'png']
dstdir = os.getcwd()

def find_pic(arg, dirname, files):
	pic_count = 0
	file_count = 0
	filepath = os.path.join(dirname, files)
	if os.path.isfile(filepath):
		file_count += 1
		filetype = os.path.splitext(files)[1][1:]
		print filetype
		if filetype in picfile:
			pic_count += 1
			shutil.copy(filepath, dstdir)
	return pic_count, file_count



def combine_pic():
	pwd = os.getcwd()
	print pwd
	c1, c2 = os.path.walk(dstdir, find_pic, None)
	print c1, c2

if "__init__" == "__main__":
	combine_pic()