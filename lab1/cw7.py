import time
import asyncio

async def gotowanie(i):
    await asyncio.sleep(5)
    print('gotowanie', i)

async def krojenie(i):
    await asyncio.sleep(2)
    print('krojenie', i)

async def smazenie(i):
    print('smazenie', i)
    await asyncio.sleep(3)

async def danie1():
    await gotowanie(1)
    await krojenie(1)
    await smazenie(1)

async def danie2():
    await smazenie(2)
    await gotowanie(2)
    await smazenie(2)

async def danie3():
    await krojenie(3)
    await gotowanie(3)
    await smazenie(3)

async def kuchnia():
    dania = await asyncio.gather(danie1(), danie2(), danie3())
    



if __name__ == "__main__":
    start = time.time()
    with asyncio.Runner() as runner:
        runner.run(kuchnia())
    print('wszystko zakonczone', time.time() - start)