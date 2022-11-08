import sys
import argparse

parser = argparse.ArgumentParser(description = 'Program that computes the factorial of a number',
	epilog = 'please ensure the input is an integer')
parser.add_argument('n', metavar = 'int', type = int, help = 'integer to calculate facotrial of')

args = parser.parse_args()
total = 1

#check to see if negative integer
if args.n < 0:
	sys.stderr.write(f'factorial.py: error: argument int: invalid negative int value {args.n}\n')
	sys.exit(1)


for i in range(1, args.n + 1):
	total *= i

print(total)
