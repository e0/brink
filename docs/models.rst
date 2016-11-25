Models
======

Models in Brink integrate seamlessly with RethinkDB, makes it a breeze to validate data and more.

Creating a model
----------------

Models simply have to inherit from the ``brink.models.Model`` class and specifiy its fields. 

::

   from brink.models import Model
   from brink import fields

   class Message(Model):
      author = fields.CharField(required=True)
      message = fields.CharField(required=True, min_length=10)

Bulding queries
---------------

You have full access to the ReQL API provided by RethinkDB.

**Fetch an item**::

   await Item.get(id)

**Delete an item**::

   await Item.get(id).delete()

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
