import asyncio

async def myCoroutine():
	print("My Coroutines")

loop = asyncio.get_event_loop()
try:
	loop.run_until_complete(myCoroutine())
finally:
	loop.close()