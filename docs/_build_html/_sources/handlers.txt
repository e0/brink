Handlers
========

Handlers handle the HTTP requests. Since brink (through aiohttp) uses Python's asyncio, we will use the ``async`` and ``await`` keywords extensively. 

Basic handler
-------------

Handlers should return two values. First the status code and second the response body.

::

   async def handle_hello(request):
      return 200, {"data": "Hello world!"}

Accessing URL parameters
------------------------

When you have a URL like ``/users/{id}`` you'd of course want to access that id in your handler.

::

   async def handle_get_user(request):
      id = request.match_info["id"]
      return 200, {"data": id}


WebSocket handlers
------------------

Writing handlers for WebSocket connections in Brink is surprisinigly easy. Unlike regular handlers, WebSocket handlers will receive two arguments. The regular ``request`` object and a special WebSocketResponse object. 


::

   async def handle_messasge_feed(request, ws):
      async for msg in Message.all().changes():
         ws.send_json(msg)
      await ws.close()

Handling request bodies
-----------------------

Handling incoming request bodies can be a hazzle. You need to parse the data, validate it and map it to your data models. In Brink this is a breeze.

::

   from brink.handlers import handle_model
   from .models import Message

   @handle_model(Message)
   async def handle_create_message(request, msg):
      await msg.save()
      return 201, msg
