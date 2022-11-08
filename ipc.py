import argparse
import subprocess

parser = argparse.ArgumentParser(
    description = "runs aacomp, captures output, reports highest and lowest frequency")

parser.add_argument("input", metavar="str", type=str, help="input sequence")
args = parser.parse_args()

output = subprocess.run(f'python3 aacomp.py {args.input}', shell=True, capture_output=True).stdout.decode().split("\n")

#removes trailing whitespace
output.pop()

maxes = {}
max = 0
mins = {}
min = 1000

#process output to find max and min
for i in range(len(output)):
    strip = output[i].rstrip()
    aa, count = strip.split()
    count = int(count)

    if count > max:
        maxes = {}
        maxes[aa] = count
        max = count

    elif count == max:
        maxes[aa] = count

    if count < min:
        mins = {}
        mins[aa] = count
        min = count
    elif count == min:
        mins[aa] = count

print("Max:")
for aa in maxes:
    print(aa,maxes[aa])

print("Min:")
for aa in mins:
    print(aa,mins[aa])
