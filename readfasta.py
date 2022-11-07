import gzip


def readfasta(fname):
	fp = None
	seqname = ""
	seq = []

	if fname.endswith(".gz"): fp = gzip.open(fname, mode = 'rt')
	else:					  fp = open(fname)

	while True:
		line = fp.readline()
		if line == '': break

		line = line.rstrip()

		if line.startswith(">"):

			if len(seq) > 0:
				yield(seqname, ''.join(seq))

				seqname = line[1:]
				seq = []
			else:
				seqname = line[1:]
		else:
			seq.append(line)
			
	yield(seqname, ''.join(seq))

	fp.close()