#
import argparse
parser = argparse.ArgumentParser()

#add arugment speficies which commandline options, in this case echo
parser.add_argument("echo", help="echo the string you use here")

parser.add_argument("square", help="display a square of a given number",
		    type=int)

#optional vse positional
parser.add_argument("--multiply", help="multiply the numbers",
		    type=int)

args = parser.parse_args()

print args.echo
print args.square**2

if args.multiply: 
	print args.multiply*args.multiply
