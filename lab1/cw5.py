import asyncio

def fib(n):
    x = 0
    for i in range(n):
        x += i
    return x

async def printing(i):
    await asyncio.sleep(i)
    print(fib(i))

async def main(N):
    L = await asyncio.gather(*[printing(i) for i in range(1, N)])

if __name__ == '__main__':
    N = 4
    with asyncio.Runner() as runner:
        runner.run(main(5))
