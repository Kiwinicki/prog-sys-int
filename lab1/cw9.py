import time
import asyncio

async def A():
    while True:
        await asyncio.sleep(2)
        print('A')

async def B():
    while True:
        await asyncio.sleep(3)
        print('B')

async def C():
    while True:
        await asyncio.sleep(5)
        print('C')

async def main():
    await asyncio.wait_for(asyncio.gather(A(), B(), C()), timeout=15)

if __name__ == '__main__':
    start = time.time()
    with asyncio.Runner() as runner:
        try:
            runner.run(main())
        except asyncio.TimeoutError:
            pass
        print(time.time() - start)

