from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TestConsumer(WebsocketConsumer):

	def connect(self):
		self.room_name = 'test_consumer'
		self.room_group_name = 'test_consumer_group'
		
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
			)
		
		self.accept()
		self.send(text_data = json.dumps({'status':'connected from test Consumers'}))

	def receive(self, text_data):
		self.send(text_data = json.dumps({'status':'we got it'}))

	def disconnect(self,  *args, **kwargs):
		print('disconnected')

	def send_notification(self, event):
		data = json.loads(event.get('value'))
		self.send(text_data=json.dumps({'payload':data}))

class NewConsumer(AsyncJsonWebsocketConsumer):

	async def connect(self):
		self.room_name = 'new_consumer'
		self.room_group_name = 'new_consumer_group'

		await(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
			)

		await self.accept()
		await self.send(text_data = json.dumps({'status':'connected from New Consumers'}))

	async def receive(self, text_data):
		await self.send(text_data = json.dumps({'status':'we got it'}))

	async def disconnect(self, *args, **kwargs):
		print('disconnected')

	async def send_notification(self, event):
		data = json.loads(event.get('value'))
		await self.send(text_data = json.dumps({'payload':data}))