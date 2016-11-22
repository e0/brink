Configuration
=============

All project configuration goes into the ``config.py`` file in the root directory
of your project.

In a default project setups without any third party applications installed, the following
settings are available.

DATABASE
--------

Database configuration for RethinkDB. Maps straight onto the native connection parameters you can pass to RethinkDB. You can find more about that `here <https://www.rethinkdb.com/api/python/connect/>`_. ::

   DATABASE = {
      "db": "test",
      "host": "localhost",
      "port": 28015
   }

MIDDLEWARE
----------

All middleware to apply to the server. Middleware works the same way as standard aiohttp middleware. ::

   MIDDLEWARE = []

INSTALLED_APPS
--------------

List of all installed apps. Both local to the project and third party. ::

   INSTALLED_APPS = [
      "brink_auth",
      "myproject"
   ]
