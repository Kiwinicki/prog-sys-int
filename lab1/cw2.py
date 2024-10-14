import asyncio

async def zad2():
    print('Hello')
    await asyncio.sleep(1)
    print('world')

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(zad2())