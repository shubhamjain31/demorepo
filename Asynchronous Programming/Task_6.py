#wait() function

import asyncio

async def myWorker():
	print("Hello Shubham")

async def main():
	print("My Main")

try:
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait([myWorker() for i in range(5)], timeout=2))
except KeyboardInterrupt:
	pass
finally:
	print("Completed All Tasks")
	loop.close()