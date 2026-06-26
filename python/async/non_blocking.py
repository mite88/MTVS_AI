# non_blocking.py
import asyncio

# 비동기 함수(async)
async def cook_ramen():
    print('라면 물 끓이기')

    await asyncio.sleep(3)  # 3초 동안 쓰레드 정지

    print("보글 보글")

async def main():
    print('요리 시작')

    task = asyncio.create_task(cook_ramen())

    print('다음 작업 수행')

    await task

    print('모든 작업 종료')

if __name__ == '__main__':
    asyncio.run(main())