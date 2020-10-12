import time

t1 = time.time()

def fetch_posts(arg):
	time.sleep(arg)
	print("Fetched all posts")

def fetch_users(arg):
	time.sleep(arg)
	print("Fetched all users")

def main():
	fetch_posts(1)
	fetch_users(2)
	print("Finished in {0:.2f} secs".format(time.time() - t1))

if __name__ == '__main__':
	main()