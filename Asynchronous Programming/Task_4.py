#as_completed() function

import asyncio

async def myWorker(number):
	return number*2

async def main(coros):
	for i in asyncio.as_completed(coros):
		print(await i)

coros = [myWorker(1) for i in range(5)]

try:
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main(coros))
except KeyboardInterrupt:
	pass
finally:
	print("Completed All Tasks")
	loop.close()