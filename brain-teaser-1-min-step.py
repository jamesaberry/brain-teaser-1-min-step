#!/usr/bin/python

import sys, getopt, subprocess, os, glob, re, datetime, shutil
from os import path
from os.path import basename

def main(argv):

	full_path = os.path.realpath(__file__)
	cur_dir = os.path.dirname(full_path)

	#get command line input or return usage
	input_file = ''
	err_output = basename(path.abspath(sys.modules['__main__'].__file__)) \
	+ ' -i <input sequence Ex: "(0, 0), (1, 1), (1, 2)">'

	try:
		opts, args = getopt.getopt(argv,"hi:v",["help", "ifile="])
	except getopt.GetoptError:
		print(err_output)
		sys.exit(2)

	if len(sys.argv) < 2:
		print(err_output)
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print(err_output)
			sys.exit()
		elif opt in ("-i", "--ifile"):
			input = arg

	#if not all populated exit
	if input == '':
		print(err_output)
		sys.exit(2)

	curx = 0
	cury = 0
	total_step_dist = 0

	# sanitize input string and split out pairs
	pair_list = input.replace(" ", "").split(",(")

	# parse over pair list max dist will be off set dist
	for pair in pair_list:
		clean_pair = pair.replace(")", "").replace("(", "").split(",")
		new_x = int(clean_pair[0])
		new_y = int(clean_pair[1])
		x_dist = abs(curx - new_x)
		y_dist = abs(cury - new_y)
		total_step_dist += x_dist if x_dist > y_dist else y_dist
		curx = new_x
		cury = new_y

	print("\nDistance traversed: " + str(total_step_dist))

if __name__ == "__main__":
   main(sys.argv[1:])
