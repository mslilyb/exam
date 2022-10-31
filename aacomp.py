import argparse


parser = argparse.ArgumentParser(description = "program to report amino acid composition alphabetically")

parser.add_argument("seq", metavar='str', type=str, help="sequence to find the composition of")

args = parser.parse_args()

aas = {}

for aa in args.seq:
	if aa in aas:
		aas[aa] += 1
	else:
		aas[aa] = 1

for aacid in sorted(aas):
	print(aacid,aas[aacid])
