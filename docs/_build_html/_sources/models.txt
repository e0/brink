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

Bulding queries
---------------

You have full access to the ReQL API provided by RethinkDB.

**Fetch an item**::

   await Item.get(id)

**Delete an item**::

   await Item.delete(id)

**Save an item**::

   item = await Item.get(id)
   item.value = False
   await item.save()

**Fetch all items**::

   await Item.all()

.. note::
   When fetching multiple items you will get an async iterator back by default. You can get a plain list instead by calling ``Item.all().as_list()`` instead.

**Fetch items where value is True**::

   await Item.filter({"value": True})

Change feeds
------------

Subscribing to a change feed is super easy. ::

   async for item in Item.all().changes():
      print(await item)

Yes. That's really it :)
