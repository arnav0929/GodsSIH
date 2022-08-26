from django.urls import re_path

from education import consumers

websocket_urlpatterns = [
    re_path('', consumers.chatconsumer.as_asgi())
]
