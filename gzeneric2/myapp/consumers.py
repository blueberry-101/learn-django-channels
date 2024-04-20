from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asyncio import sleep as asleep
from time import sleep
class MyWSconsumer(WebsocketConsumer):
    def connect(self):
        return super().connect()
    
    def receive(self, text_data=None, bytes_data=None):

        for i in range(10):
            sleep(1)
            self.send(text_data=str(i))

        # return super().receive(text_data, bytes_data)
    
    def disconnect(self, code):
        return super().disconnect(code)


class MyAWSconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        return await super().connect()
    
    async def receive(self, text_data=None, bytes_data=None):
        for i in range(10):
            await asleep(1)
            await self.send(text_data=str(i))
        return await super().receive(text_data, bytes_data)
    
    async def disconnect(self, code):
        return await super().disconnect(code)