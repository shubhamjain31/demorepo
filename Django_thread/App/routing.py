from django.urls import re_path
from django.urls import path

from . import consumer

websocket_urlpatterns = [
    # re_path(r'ws/test/', consumers.TestConsumer)
    path('ws/test/', consumer.TestConsumer.as_asgi())
]