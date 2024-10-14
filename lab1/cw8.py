import asyncio

async def wczytanie():
    await asyncio.sleep(2)
    print('wczytanie')

async def analiza():
    await asyncio.sleep(4)
    print('analiza')

async def zapis():
    await asyncio.sleep(1)
    print('zapis')

async def przetwarzanie1():
    await wczytanie()
    await analiza()
    await zapis()

async def przetwarzanie2():
    await wczytanie()
    await analiza()
    await analiza()
    await zapis()

async def przetwarzanie3():
    await wczytanie()
    await analiza()
    await wczytanie()
    await zapis()

async def main():
    pliki = await asyncio.gather(przetwarzanie1(), przetwarzanie2(), przetwarzanie3())


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(main())