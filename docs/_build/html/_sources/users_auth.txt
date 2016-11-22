Users and Authentication
========================

Brink Auth will add a User model to your project, along with a list of API endpoints to interact with it. It also adds an authentication endpoint where the API consumer can obtain a JWT token by providing user credentials. Brink Auth also (soon) includes a number of handler decorators to restrict handlers to authenticated users, and possibly only with specific roles.

Installation
------------

Install Brink Auth with pip as such

::

   $ pip install brink-auth

and then add it to your installed apps


::

   INSTALLED_APPS = [
      "brink_auth",
      # ...
   ]

Configuration
-------------

None at the moment.

Decorators
----------

TBD

API Endpoints
-------------

:POST:
   ``/auth``
      Authenticate by a user

      Request body::

         {
            "username": "gunnar",
            "password": "pass"
         }
:GET:
   ``/users``
      Returns a list of all users
:POST:
   ``/users``
      Create a new user

      Request body::

         {
            "username": "gunnar",
            "password": "pass"
         }

:GET:
   ``/users/{id}``
      Get a single user by id
:PUT:
   ``/users/{id}``
      Update a user with id
:DELETE:
   ``/users/{id}``
      Delete a user by id






