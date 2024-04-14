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

        
        await self.send({
            "type":"websocket.send",
            "text":"message from server"
        })
        print("self",self)
        print("event",event)

        # print("channel name",self.scope) 
        """
        {'type': 'websocket', 'path': '/ws/ac/', 'raw_path': b'/ws/ac/', 'headers': [(b'host', b'127.0.0.1:8000'), (b'connection', b'Upgrade'), (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), (b'user-agent', b'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'), (b'accept-language', b'en-US,en'), (b'upgrade', b'websocket'), (b'origin', b'http://127.0.0.1:8000'), (b'sec-websocket-version', b'13'), (b'accept-encoding', b'gzip, deflate, br, zstd'), (b'sec-websocket-key', b'Xjj78KbHhaQNz3O2aFsI9A=='), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits')], 'query_string': b'', 'client': ['127.0.0.1', 59936], 'server': ['127.0.0.1', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}, 'path_remaining': '', 
        'url_route': {'args': (), 'kwargs': {}}}
        """
        


    async def websocket_disconnect(self, event):
        print("Disconnected", event)

        raise StopConsumer()
