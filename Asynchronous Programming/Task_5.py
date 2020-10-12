#gather() function

import asyncio

async def myWorker():
	print("Hello Shubham")

async def main():
	print("My Main")

try:
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.gather(*[myWorker() for i in range(5)]))
except KeyboardInterrupt:
	pass
finally:
	print("Completed All Tasks")
	loop.close()