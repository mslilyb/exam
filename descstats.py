import sys
import math

values = []

for arg in sys.argv[1:]:
	if arg.isdigit():
		values.append(int(arg))
	else: print(arg,"is not a valid integer", file = sys.stderr)

values = sorted(values)


#mean
total = 0
count = 0
for i in values:
	total += i
	count += 1

mean = total / count

print("mean: ",mean)

#median

if len(values) % 2 != 0:
	mcoord = math.ceil(len(values) / 2 - 1)
	print("median: ", values[mcoord])
else:
	low = int(len(values) / 2 - 1)
	high = low + 1

	median = (values[low] + values[high]) / 2
	print("median: ", median)

#stdev
variance = 0

for i in values:
	variance += (i - mean) ** 2

variance = variance / count

stdev = math.sqrt(variance)

print("stdev: ",stdev)
