import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i + 1}-й шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Michailo', 3))
    task2 = asyncio.create_task(start_strongman('Perejro', 4))
    task3 = asyncio.create_task(start_strongman('Urchailo', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())






