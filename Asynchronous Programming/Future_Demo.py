import asyncio

async def myCoroutine(future):
	await asyncio.sleep(1)
	future.set_result("My coroutine turned future has completed")

async def main():
	future = asyncio.Future()
	await asyncio.ensure_future(myCoroutine(future))
	print(future.result())

loop = asyncio.get_event_loop()
try:
	loop.run_until_complete(main())
except:
	pass
finally:
	loop.close()