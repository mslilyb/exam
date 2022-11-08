import sys
import gzip

#overlap finding function
def findoverlap(beg1, end1, beg2, end2):
	if beg1 < end2 and end1 > beg2: return True
	else: 							return False


#reads .gff filetype
def readgff(fname):
	if fname.endswith(".gz"): fp = gzip.open(fname, mode = "rt")
	else:				      fp = open(fname)

	records = []

	while True:
		line = fp.readline()
		if line == '': break

		line = line.rstrip()

		fields = line.split()
		record = {}
		record["chrom"] = fields[0]
		record["beg"] = int(fields[3])
		record["end"] = int(fields[4])
		records.append(record)
	fp.close()
	return records



#read two different files
f1records = readgff(sys.argv[1])
f2records = readgff(sys.argv[2])

#find overlap between them
for f1r in f1records:
	for f2r in f2records:
		if f1r["chrom"] != f2r["chrom"]: continue
		if findoverlap(f1r["beg"], f1r["end"], f2r["beg"], f2r["end"]):
			print(f'Chr {f1r["chrom"]}: {f1r["beg"]} - {f1r["end"]} overlaps {f2r["beg"]} - {f2r["end"]}')
