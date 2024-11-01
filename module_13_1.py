import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(5):
        await asyncio.sleep(10//power)
        print(f"Силач {name} поднял {i+1} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Вася", 2))
    task2 = asyncio.create_task(start_strongman("Коля", 3))
    task3 = asyncio.create_task(start_strongman("Петя", 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())