# future.py
import asyncio

async def explain_future():
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    print(f'future={future.done()}')

    async def set_result_later():
        await asyncio.sleep(1)
        future.set_result('Future의 결과값')

    asyncio.create_task(set_result_later())

    result = await future

    print(f'future의 결과값={result}')
    print(f'future의 상태={future.done()}') # True

if __name__ == "__main__":
    asyncio.run(explain_future())