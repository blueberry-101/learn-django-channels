from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from myapp.models import Chats,Group
from channels.db import database_sync_to_async

class MyWSconsumer(WebsocketConsumer):
    def connect(self):
        channel_name = self.channel_name  # 1
        kwargs = self.scope.get("url_route").get("kwargs")
        self.group_name = kwargs.get("group_name")  # 2
        scope = self.scope
        """
            channel scope {'type': 'websocket', 'path': '/ws/gwc/in/12/', 'raw_path': b'/ws/gwc/in/12/', 'headers': [(b'sec-websocket-version', b'13'), (b'sec-websocket-key', b'SMpj+yx4upqPy7xmwp4j8g=='), (b'connection', b'Upgrade'), (b'upgrade', b'websocket'), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits'), (b'host', b'127.0.0.1:8000')], 'query_string': b'', 'client': ['127.0.0.1', 57701], 'server': ['127.0.0.1', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}, 'path_remaining': '', 'url_route': {'args': (), 'kwargs': {'groupname': 'in', 'number': 12}}}
        """
        print("channel name",channel_name)
        print("channel group name",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            channel_name
        )

        print(self.groups)  # RedisChannelLayer(hosts=[{'address': ('localhost', 6379)}])
        

        return super().connect()
    
    def receive(self, text_data=None, bytes_data=None):
        message_dict = json.loads(text_data)
        # code for saving data in group
        group = Group.objects.get(name = self.group_name)
        chat_model = Chats(
            group = group,
            texts = message_dict.get("msg")
        )
        chat_model.save()
        ##
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type":"message.send",
                "message":message_dict.get("msg")
            }
        )
        return super().receive(text_data, bytes_data)
    
    def message_send(self,event):
        self.send(
            text_data=json.dumps(
                {
                    "msg":event.get("message")
                }
            )
            )
        print(event)  # {'type': 'message.send', 'message': 'Hi I u are using postman'}
     
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        return super().disconnect(code)


class MyAWSconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        channel_name = self.channel_name  # 1
        kwargs = self.scope.get("url_route").get("kwargs")
        self.group_name = kwargs.get("group_name")  # 2
        scope = self.scope
        """
            channel scope {'type': 'websocket', 'path': '/ws/gwc/in/12/', 'raw_path': b'/ws/gwc/in/12/', 'headers': [(b'sec-websocket-version', b'13'), (b'sec-websocket-key', b'SMpj+yx4upqPy7xmwp4j8g=='), (b'connection', b'Upgrade'), (b'upgrade', b'websocket'), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits'), (b'host', b'127.0.0.1:8000')], 'query_string': b'', 'client': ['127.0.0.1', 57701], 'server': ['127.0.0.1', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}, 'path_remaining': '', 'url_route': {'args': (), 'kwargs': {'groupname': 'in', 'number': 12}}}
        """
        print("channel name",channel_name)
        print("channel group name",self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            channel_name
        )

        print(self.groups)  # RedisChannelLayer(hosts=[{'address': ('localhost', 6379)}])
        

        return await super().connect()
    
    async def receive(self, text_data=None, bytes_data=None):
        message_dict = json.loads(text_data)
        # code for saving data in group
        group = await database_sync_to_async(Group.objects.get)(name = self.group_name)
        chat_model = Chats(
            group = group,
            texts = message_dict.get("msg")
        )
        await database_sync_to_async(chat_model.save)()

        #  await database_sync_to_async(chat_model.save()) not possible
        
        ##

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type":"message.send",
                "message":message_dict.get("msg")
            }
        )
        return await super().receive(text_data, bytes_data)
    
    async def message_send(self,event):
        await self.send(
            text_data= json.dumps(
                {
                    "msg":event.get("message")
                }
            )
            )
        print(event)  # {'type': 'message.send', 'message': 'Hi I u are using postman'}
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        return await super().disconnect(code)