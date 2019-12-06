import asyncio
import concurrent

from serial import Serial

# Normal serial blocking reads
# This could also do any processing required on the data
def get_byte():
        return s.read(1)

    # Runs blocking function in executor, yielding the result
    @asyncio.coroutine
    def get_byte_async():
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            res = yield from loop.run_in_executor(executor, get_byte)
            return res

def get_and_print():
    b = yield from get_byte_async()
    print (b)

s = Serial("COM11", 19200, timeout=10)
loop = asyncio.get_event_loop()
loop.run_until_complete(get_and_print())
