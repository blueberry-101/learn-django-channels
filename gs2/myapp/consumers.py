from channels.consumer import SyncConsumer,AsyncConsumer,StopConsumer
from time import sleep
from asyncio import sleep as asleep
class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("Connected...",event)
        self.send({
            "type":"websocket.accept"
        })

    def websocket_receive(self,event):
        print("received message",event)

        for i in range(30):
            self.send({
                "type":"websocket.send",
                "text":str(i)

            })
            sleep(1)


    def websocket_disconnect(self,event):
        print("Disconnected",event)


class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("Connected...", event)
        await self.send({
            "type": "websocket.accept"
        })
    
        
    async def websocket_receive(self, event):
        print("received message", event)

        for i in range(30):
            await self.send({
                "type":"websocket.send",
                "text":str(i)

            })
            await asleep(1)

    async def websocket_disconnect(self, event):
        print("Disconnected", event)
        raise StopConsumer()
