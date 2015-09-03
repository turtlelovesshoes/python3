# 1 create program that takes in 2 numbers and adds them and returns th answer

import argparse
parser = argparse.ArgumentParser(description='take in 2 numbers and do something')
parser.add_argument('-a','--alpha', type=int,
                   help='an integer for the accumulator')
parser.add_argument('-b','--omega', type=int, help='an integer for the accumulator')
args = parser.parse_args()
print args
print args.omega - args.alpha
