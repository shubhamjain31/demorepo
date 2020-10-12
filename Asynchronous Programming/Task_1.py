import asyncio
import time

async def myTask():
	time.sleep(1)
	print("Processing Task")

async def myTaskGenerator():
	for i in range(5):
		asyncio.ensure_future(myTask())

loop = asyncio.get_event_loop()
try:
	loop.run_until_complete(myTaskGenerator())
except:
	pass
finally:
	print("Completed All Tasks")
	loop.close()