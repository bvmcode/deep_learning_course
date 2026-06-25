import asyncio


async def async_function(sleep_time=1):
    await asyncio.sleep(sleep_time)
    print(f"Finished sleeping for {sleep_time} seconds")
    return f"Result after sleeping for {sleep_time} seconds"

async def main():
    task = asyncio.create_task(async_function(2))
    task2 = asyncio.create_task(async_function(1))
    resp1 = await task
    resp2 = await task2
    print(resp1)
    print(resp2)

if __name__ == "__main__":
    asyncio.run(main())
