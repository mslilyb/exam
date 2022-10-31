import random 

birthdays = []
i = 0
match = False

while True:
	birthday = random.randint(1, 365)
	birthdays.append(birthday)
	i += 1

	for j in range(len(birthdays) - 1):
		if i != 1 and birthdays[j] == birthday:
			print(i,"people")
			match = True

	if match:
		break