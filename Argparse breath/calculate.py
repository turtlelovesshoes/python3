# Assign Aug 11, 2015 
#Ilana mentorship
#create a python program that takes in an arbitrary length of numbers and returns the sum or the product or both
#Finished August 26, 2015
import argparse 
import itertools

parser = argparse.ArgumentParser(description='take in any number of numbers and do something')
#parser to take in the arbitry integers
parser.add_argument('integers', metavar='N', type=int, nargs='+',
					help='an integer for the accumulator')
#argument to multiply them
parser.add_argument('-a','--adding',action='store_true',
					help='integers that are added')
#argurment to add them
parser.add_argument('-m','--multiply',action='store_true',
					help='integers that are multiplied')

args = parser.parse_args()
summ=0
product = 1

if args.integers:
	print "These are {} ".format(args.integers)

#if the value is true in namespace do this
if args.adding:
	#reset pointer
	i = 0
	while (i < len(args.integers)):
	#	print i
		summ+=args.integers[i]
		i+=1
	print summ

#if the value is true in namespace do this
if args.multiply:
	#reset pointer
	i = 0
	while(i < len(args.integers)):
		product*=args.integers[i]
		i+=1
	print product
#version 3.4
#print (args.product(args.integers, operator.mul))
#print args
