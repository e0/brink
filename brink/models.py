import rethinkdb as r
from inflection import tableize
from cerberus import Validator
from brink.db import conn


class ObjectManager(object):

    def __init__(self, model_cls, table_name):
        self.model_cls = model_cls
        self.query = r.table(table_name)

    def exclude(self, *args):
        self.query = self.query.without(*args)
        return self

    async def all(self, generator=True):
        if generator:
            return self.__generator
        else:
            items = []
            async for item in self.__generator():
                items.append(item)
            return items

    async def get(self, id):
        return self.__wrap(await self.query.get(id).run(await conn.get()))

    async def __generator(self):
        cursor = await self.query.run(await conn.get())
        while await cursor.fetch_next():
            yield self.__wrap(await cursor.next())

    def __wrap(self, data):
        model = self.model_cls()
        model.data.update(data)
        return model


class MetaModel(type):

    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        table_name = tableize(name)
        setattr(new_cls, "objects", ObjectManager(new_cls, table_name))
        setattr(new_cls, "table_name", table_name)
        return new_cls

    def __getattr__(self, attr):
        return getattr(self.objects, attr)


class UndefinedSchema(Exception):
    pass


class ValidationError(Exception):

    def __init__(self, errors):
        self.errors = errors


class Model(object, metaclass=MetaModel):

    schema = None
    data = {}

    def validate(self):
        if self.schema is None:
            raise UndefinedSchema()

        v = Validator(self.schema)

        if not v.validate(self.data):
            raise ValidationError(v.errors)

        return True

    async def save(self):
        pass

    async def delete(self):
        pass

    def __getattr__(self, attr):
        return self.data[attr]

    def __setattr__(self, attr, value):
        self.data[attr] = value

    def __json__(self):
        return self.data

