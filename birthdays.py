import random

counts = {}
results = []

#repeat 10000 times to get consistent answer
for r in range(10000):
	match = False
	birthdays = []
	counts[r] = 0
	i = 0
	while True:
		birthday = random.randint(1, 365)
		birthdays.append(birthday)
		i += 1

		for j in range(len(birthdays) - 1):
			if i != 1 and birthdays[j] == birthday:
				match = True

		if match:
			results.append(i)
			break

for result in results:
	counts[result] += 1


mode = 0
modecount = 0
mean = 0
total = 0

#find mean and mode
for num in counts:
	if counts[num] > modecount:
		mode = num
		modecount = counts[num]

	total += num * counts[num]


mean = total / 10000
print("mean:", mean, " mode:", mode)
