from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/like/(?P<room_name>\w+)/$', consumers)
]