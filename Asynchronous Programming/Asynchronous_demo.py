import time
import asyncio

t1 = time.time()

async def fetch_posts(arg):
	await asyncio.sleep(arg)
	print("Fetched all posts")

async def fetch_users(arg):
	await asyncio.sleep(arg)
	print("Fetched all users")

async def main():
	await asyncio.gather(fetch_posts(2),fetch_users(1))
	print("Finished in {0:.2f} secs".format(time.time() - t1))

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())