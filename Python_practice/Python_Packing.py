def Sum(*args):
	sum = 0
	for i in range(0, len(args)):
		sum = sum + args[i]
	return sum

print("Function with 4 arguments & Sum is: \n",Sum(9, 1,6,2))
print("Function with 5 arguments & Sum is: \n",Sum(2, 3, 4, 5, 6))
print("Function with 6 arguments & Sum is: \n",Sum(20, 30, 40, 12, 40, 54))