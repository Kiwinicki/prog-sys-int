import time
import asyncio

async def czekanie(i):
    await asyncio.sleep(i)
    print(f'{i} sek')

async def main():
    await asyncio.gather(czekanie(3), czekanie(4))

if __name__ == "__main__":
    start = time.time()
    with asyncio.Runner() as runner:
        runner.run(main())
    print(time.time() - start)

