import asyncio

async def myCoroutine():
	print("Coroutine 1")

@asyncio.coroutine
def func():
	print("Coroutine 2")