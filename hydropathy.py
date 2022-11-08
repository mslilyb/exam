import argparse
import sys

#initialize hydrophilicity dictionary, using Kyte-Doolittle
aacids = {
	"I": 4.5,
	"V": 4.2,
	"L": 3.8,
	"F": 2.8,
	"C": 2.5,
	"M": 1.9,
	"A": 1.6,
	"G": -0.4,
	"T": -0.7,
	"S": -0.8,
	"W": -0.9,
	"Y": -1.3,
	"P": -1.6,
	"H": -3.2,
	"E": -3.5,
	"Q": -3.5,
	"D": -3.5,
	"N": -3.5,
	"K": -3.9,
	"R": -4.5
}

parser = argparse.ArgumentParser(description = "program to find hydropathy of an amino acid sequence in sliding windows")

parser.add_argument("window", metavar='int', type=int, help="window size")
parser.add_argument("seq", metavar='str', type=str, help="sequence to find hydropathy of")

args = parser.parse_args()

results = {}

#Calculate hydopathy in window
for i in range(len(args.seq) - args.window + 1):
	position1 = i + 1
	position2 = i + args.window
	selection = args.seq[i:position2]
	
	total = 0 
	for aa in selection:
		if aa in aacids:
			total += aacids[aa]
		else:
			print("Illegal amino acid ",aa," in sequence.", file=sys.stderr)

	results[(position1, position2)] = total

print("Pos(start,end)\tScore")
for pos in results:
	print(pos,"\t",results[pos])

