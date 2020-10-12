import asyncio
import time

async def myWorker(lock):
    print("Attempting to attain lock")
    ## acquire lock
    async with lock:
        #run critical section of code
        print("Currently Locked")
        time.sleep(2)
    #our worker releases lock at this poit
    print("Unlocked Critical Section")

async def main():
    #instantiate our lock
    lock = asyncio.Lock()
    #await the execution of 2 myWorker coroutines each with our same lock instance passed in
    await asyncio.wait([myWorker(lock), myWorker(lock)])

## Start up a simple loop and run our main function until it is complete
lock = asyncio.Lock()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("All Tasks Completed")
loop.close()