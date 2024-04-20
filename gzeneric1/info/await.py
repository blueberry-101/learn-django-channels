import asyncio

class AwaitableObject:
    def __await__(self):
        # Returning an iterator that yields a coroutine object
        async def coroutine():
            await asyncio.sleep(1)
            return "Hello, World!"
        
        return coroutine().__await__()

async def main():
    awaitable_obj = AwaitableObject()
    result = await awaitable_obj
    print(result)

asyncio.run(main())
