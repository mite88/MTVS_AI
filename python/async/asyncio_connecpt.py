# asyncio_connecpt.py

import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    await asyncio.gather(
        say_after(1, "1초뒤 출력"),
        say_after(2, "2초뒤 출력"),
        say_after(3, "3초뒤 출력")
    )

if __name__ == "__main__":
    asyncio.run(main())