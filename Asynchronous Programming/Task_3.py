#cancel() function

import asyncio
import time

async def myTask():
	time.sleep(1)
	print("Processing Task")
	for task in asyncio.all_tasks():
		print(task)
		task.cancel()
		print(task)

async def main():
	for i in range(5):
		asyncio.ensure_future(myTask())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Completed All Tasks")
loop.close()