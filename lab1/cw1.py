import asyncio

async def zad1():
    await asyncio.sleep(2)
    print('Oczekiwanie zakończone')

if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(zad1())