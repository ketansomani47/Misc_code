# import asyncio
# def get_chat_id(name):
#     # time.sleep(3)
#     return "chat-%s" % name
#
# def main():
#     result = get_chat_id("django")
#     return result
#
# x = main()
# print(x)
# print(get_chat_id)
# import asyncio
#
# async def main(x):
#     print('Hello ...', x)
#     await asyncio.sleep(10)
#     print('... World!')
#
# for i in range(10):
#     asyncio.run(main(i))
import asyncio
async def async_func():
    print('Velotio ...')
    await asyncio.sleep(5)
    print('... Blog!')

async def main():
    print("testing")
    # await async_func()
    task = asyncio.create_task(async_func())
    print("done!!!!")

asyncio.run(main())