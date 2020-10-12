import asyncio
import time

def myTask():
	time.sleep(1)
	print("Processing Task")

def myTaskGenerator():
	for x in range(5):
		myTask()

myTaskGenerator()
print("Completed All Tasks")