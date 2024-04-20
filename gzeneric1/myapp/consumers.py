from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asyncio import sleep
class MyWSconsumer(WebsocketConsumer):
    def connect(self):
        # self.close()
        return super().connect()
    
    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        self.send(
            text_data="bye"
        )
        print(bytes_data)
        return super().receive(text_data, bytes_data)
    
    def disconnect(self, code):
        print("disconnected",code)
        return super().disconnect(code)

class MyAWSconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        await sleep(4)  # not causing disconnection
        await sleep(5)  # causing disconnection
        """
        return await super().connect()
    
    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        """
        await sleep(10)  # not causing disconnection
        """
        await self.send(
            text_data="bye"
        )
        print(bytes_data) #  gives none
        return await super().receive(text_data, bytes_data)
    
    async def disconnect(self, code):
        print("disconnected",code)
        return await super().disconnect(code)
    
    