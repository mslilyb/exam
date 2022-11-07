import sys
import random

count = int(sys.argv[1])
chrcount = int(sys.argv[2])
chrlen = int(sys.argv[3])



for i in range(count):
	chrom = random.randrange(1, chrcount + 1, 1)
	beg = random.randrange(1, chrlen + 1, 1)
	end = random.randrange(beg, chrlen + 1, 1)
	print(f'{chrom}	type	feature	{beg}	{end}')