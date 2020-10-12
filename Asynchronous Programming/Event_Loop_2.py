import asyncio
import time

async def myCoroutine():
	print("Starting Work")
	time.sleep(5)
	print("Finishing Work")

loop = asyncio.get_event_loop()
try:
	loop.run_until_complete(myCoroutine())
finally:
	loop.close()