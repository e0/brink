import rethinkdb as r
from inflection import tableize
from cerberus import Validator
from brink.db import conn
import copy


class ObjectManager(object):

    def __init__(self, model_cls, table_name):
        self.model_cls = model_cls
        self.table_name = table_name

    def all(self):
        return ObjectSet(self.model_cls, r.table(self.table_name))

    def filter(self, *args, **kwargs):
        return self.all().filter(*args, **kwargs)

    async def get(self, id):
        return self.model_cls(
            **(await r.table(self.table_name).get(id).run(await conn.get())))

    async def delete(self, id):
        await r.table(self.table_name).get(id).delete().run(await conn.get())


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

class UnexpectedDbResponse(Exception):

    pass


class Model(object, metaclass=MetaModel):

    schema = None
    data = {}

    def __init__(self, **kwargs):
        self.data = kwargs

    def validate(self):
        if self.schema is None:
            raise UndefinedSchema()

        v = Validator(self.schema)

        if not v.validate(self.data):
            raise ValidationError(v.errors)

        return True

    async def save(self):
        if hasattr(self, 'before_save'):
            self.before_save()

        query = r.table(self.table_name)

        if hasattr(self, "id"):
            query = query.get(self.id).replace(self.data, return_changes=True)
        else:
            query = query.insert(self.data, return_changes=True)

        resp = await query.run(await conn.get())

        try:
            self.replace(resp['changes'][0]['new_val'])
        except KeyError:
            raise UnexpectedDbResponse()

        return self

    async def delete(self):
        self.__class__.delete(self.id)

    def patch(self, data):
        self.data.update(data)
        return self

    def replace(self, data):
        self.data = {}
        self.data.update(data)
        return self

    def __getattr__(self, attr):
        try:
            return self.data[attr]
        except KeyError as e:
            raise AttributeError(attr)

    def __delattr__(self, attr):
        try:
            del self.data[attr]
        except KeyError:
            raise AttributeError(attr)

    def __getitem__(self, attr):
        return self.data[attr]

    def __setitem__(self, attr, value):
        self.data[attr] = value

    def __delitem__(self, attr):
        del self.data[attr]

    def __json__(self):
        return self.data


class ObjectSet(object):

    cursor = None

    def __init__(self, model_cls, query):
        self.query = query
        self.model_cls = model_cls
        self.returns_changes = False

    def changes(self):
        self.query = self.query.changes()
        self.returns_changes = True
        return self

    async def as_list(self):
        return [obj async for obj in self]

    async def run(self):
        return await self.query.run(await conn.get())

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.cursor is None:
            self.cursor = await self.query.run(await conn.get())

        if (await self.cursor.fetch_next()):
            data = await self.cursor.next();

            if self.returns_changes:
                data = data["new_val"]

            return self.model_cls(**data)
        else:
            raise StopAsyncIteration

    def __getattr__(self, attr):
        def func_proxy(*args, **kwargs):
            self.query = getattr(self.query, attr)(*args, **kwargs)
            return self
        return func_proxy
        

