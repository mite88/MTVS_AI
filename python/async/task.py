#task.py
import asyncio

async def worker(name, delay):
    print(f'{name} : 작업시작')
    await asyncio.sleep(delay)
    print(f'{name} : 작업종료')
    return f'worker {name} 결과물'


async def main():
    # 코루틴이라 await 붙음
    # 근데 이렇게 하면 동기 실행이 되어버림
    #await worker('작업자1', 2)
    #await worker('작업자2', 1)

    task1 = asyncio.create_task(worker('작업자1', 2))
    task2 = asyncio.create_task(worker('작업자2', 1))

    result1 = await task1
    result2 = await task2
    print(f"결과: {result1}, {result2}")


if __name__ == '__main__':
    asyncio.run(main())
