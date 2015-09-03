""" 

Assignment from August 11, 2015
create a program that you give name of input and output file.
the program reads the input info and prints to the output feel 
and removes the letter b 
"""
# learned
#fake argument, create your own namespace --whatt?? 

import argparse

parser = argparse.ArgumentParser(description='Read the end of a file')
parser.add_argument('-i', action="store", dest="input_file",
					help='this is the filename and path argument')
parser.add_argument('-o', action="store", dest="output_file",
					help='this is the filename and path argument')
parser.add_argument('-s',action='store_true',
					help='replace the letter b with smilies :-)')

args = parser.parse_args()
b = "b"

#file_object = open(filename, mode)
#does input and output codec matter? 
print args.input_file
print args.output_file
file_object = open(args.input_file, "r+")
file_dest = open(args.output_file, "w")

#added smilies option to make it fun
if args.s:
	for line in file_object:
		#print line
		line = line.replace('b', ':-)')
		file_dest.write(line)
else:
	for line in file_object:
		#print line
		line = line.replace('b', '')
		file_dest.write(line)


file_object.close()
file_dest.close()
