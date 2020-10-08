dictionary = {}
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1

sum = 0
for i in dictionary:
	sum += dictionary[i]
print(sum)