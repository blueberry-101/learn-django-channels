from channels.consumer import SyncConsumer,AsyncConsumer,StopConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("Connected...",event)
        self.send({
            "type":"websocket.accept"
        })

    def websocket_receive(self,event):
        print("received message",event)

        # self.send({
        #     "type":"text",

        # })

    def websocket_disconnect(self,event):
        print("Disconnected",event)

class MyAsyncConsumer(AsyncConsumer):

    
        
    async def websocket_receive(self, event):
        print("received message", event)

    async def websocket_connect(self, event):
        print("Connected...", event)
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)
        raise StopConsumer()
