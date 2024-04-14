from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("Connected...", event)
        print("Channel Layer",self.channel_layer)
        print("Channel Layer",self.channel_name)
        self.send({
            "type": "websocket.accept"
        })
    #      group
        async_to_sync(self.channel_layer.group_add)(
            "programmers",
            self.channel_name
        )
        

    def websocket_receive(self, event):
        print("received message", event)

        
    #    send message to group
        async_to_sync(self.channel_layer.group_send)("programmers",
        {
            "type":"chat.message",
            "message" : event["text"]

        })

    def chat_message(self,event):
        print("Event...",event)
        self.send({
            "type":"websocket.send",
            "text":event["message"]
        })


    def websocket_disconnect(self, event):
        print("Disconnected", event)
    
    #   channels info

        print("Channel disconnected",self.channel_name)
        print("channels layer",self.channel_layer)

        
    
    #   discard the group
        async_to_sync(self.channel_layer.group_discard)(
            "programmers",
            self.channel_name
        )

        raise StopConsumer()
    

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Connected...", event)
        print("Channel Layer",self.channel_layer)
        print("Channel Layer",self.channel_name)
        await self.send({
            "type": "websocket.accept"
        })
    #      group
        await self.channel_layer.group_add(
            "programmers",
            self.channel_name
        )
        

    async def websocket_receive(self, event):
        print("received message", event)

        
    #    send message to group
        await self.channel_layer.group_send("programmers",
        {
            "type":"chat.message",
            "message" : event["text"]

        })

    async def chat_message(self,event):
        print("Event...",event)
        await self.send({
            "type":"websocket.send",
            "text":event["message"]
        })


    async def websocket_disconnect(self, event):
        print("Disconnected", event)
    
    #   channels info

        print("Channel disconnected",self.channel_name)
        print("channels layer",self.channel_layer)

        
    
    #   discard the group
        await self.channel_layer.group_discard(
            "programmers",
            self.channel_name
        )

        raise StopConsumer()