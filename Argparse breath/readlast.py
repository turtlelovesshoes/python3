# Assignment from Ilana 
#Create program where you feed it the name of the file and it gives you the last line of the file

import argparse

parser = argparse.ArgumentParser(description='Read the end of a file')
parser.add_argument('-f', action="store", dest= "filename",
					help='this is the filename and path argument')

args = parser.parse_args()

print args.filename

#file_object = open(filename, mode)
#open the file for reading and writing
file_object = open(args.filename, 'r+')
print file_object.readlines()[-1]
#or less efficient
#for line in file_object:
#	print line
file_object.close()




