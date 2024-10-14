import asyncio

async def fetch(delay: int):
    await asyncio.sleep(delay)
    return delay


async def main():
    L = await asyncio.gather(*[fetch(i) for i in range(5)])
    print(L)


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(main())