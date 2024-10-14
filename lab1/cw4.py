import asyncio

async def zad4(i):
    await asyncio.sleep(i)
    print(i)


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        for i in range(1, 5):
            runner.run(zad4(i))