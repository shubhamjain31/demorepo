values = [1,2,3,3,4]
numbers = set(values)

def checknums(num):
	if num in numbers:
		return True
	else:
		return False
	
for i in filter(checknums, values):
	print(i)