#function with three argument
def func1(x,y,z):
	print("Argument One: ",x)
	print("\nArgument Two: ",y)
	print("\nArgument Three: ",z)

#Packing- All arguments passed to func2 are packed into tuple *args
def func2(*args):

	#To do some modification, we need to convert args tuple to list
	args = list(args)
	
	#Modifying args[0] & args[1]
	args[0] = 'Hello'
	args[1] = 'Shubham'
	
	#Unpacking args and calling func1()
	func1(*args)

#Driver code
func2("I", "Love", "Coding")