URLs
====

URLs or routes are specified on a per app basis. They should be specified in a file named ``urls.py`` in the root directory of each **app**. 

The ``urls.py`` file should contain a variable also names urls. It should hold a list of all the URLs for the app and a reference to their respective handler. This is accomplished by using special functions, named after each HTTP verb. The functions can be imported from the ``brink.urls`` module.

.. note::
   When setting URLs for websocket connections, the handler function needs to be implemented differently. See :ref:`handlers`.

Example
-------
::

   from brink.urls import GET, POST, WS

   urls = [
      GET("/greet", "handlers.handle_hello"),
      POST("/greeings", "handlers.handle_add_greeting"),
      WS("/greetings", "handlers.handle_greetings_feed")
   ]
