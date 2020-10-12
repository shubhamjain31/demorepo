import asyncio

async def speak():
	print("OMG asynchronicity!")

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(speak())
	loop.close()