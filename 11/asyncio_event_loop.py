import asyncio

async def my_coroutine():
    print("Start my coroutine")
    await asyncio.sleep(2)
    print("End my coroutine")


async def another_coroutine():
    print("Start another coroutine")
    await asyncio.sleep(1)
    print("End another coroutine")


async def main():
    await asyncio.gather(my_coroutine(), another_coroutine())
    print("test")

asyncio.run(main())
