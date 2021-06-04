# Asynchronous
import requests
import threading
import time
import concurrent.futures

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80000
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")


# Synchronous
# sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80

# start_time = time.time()

# for i in sites:
#     response = requests.get(i)
#     print(f"Read {len(response.content)} from {i}")

# duration = time.time() - start_time
# print(f"Downloaded {len(sites)} in {duration} seconds")