Models
======

Models in Brink integrate seamlessly with RethinkDB, makes it a breeze to validate data and more.

Creating a model
----------------

Models simply have to inherit from the ``brink.models.Model`` class and provide a schema to be used for validation. The schema should be specified according to the Cerberus_ validator specification. 

::

   from brink.models import Model

   class Message(Model):
      schema = {
         "author": {"type": "string", "required": True},
         "message": {"type": "string", "required": True, "minlength": 10}
      }

.. _Cerberus: http://docs.python-cerberus.org/en/stable/
