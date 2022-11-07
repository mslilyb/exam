import sys
import gzip

def findoverlap(beg1, end1, beg2, end2):
	if beg1 < end2 and end1 > beg1: return True
	else: 							return False



def readgff(fname):
	if fname.endswith(".gz"): fp = gzip.open(fname, mode = "rt")
	else:				      fp = open(fname)

	records = []

	while True:
		line = fp.readline()
		if line == '': break

		line = line.rstrip()

		fields = line.split()

	fp.close()




readgff(sys.argv[1])