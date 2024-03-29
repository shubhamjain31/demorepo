from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from App import routing
import App.routing


application = ProtocolTypeRouter({

    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            App.routing.websocket_urlpatterns
        )
    ),
})
