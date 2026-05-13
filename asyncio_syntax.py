import asyncio
import time 

async def greet(name:str="vic") -> str:
    await asyncio.sleep(5)
    print (f"Hello {name}")

async def greet2(name:str="Shan") -> str:
    await asyncio.sleep(3)
    print(f"Good morning {name}")


async def main():
    await asyncio.gather(
        greet(),
        greet2()
    )

asyncio.run(main())