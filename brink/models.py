from remodel import models
from remodel import object_handler
import rethinkdb


class ObjectHandler(object_handler.ObjectHandler):
    def exclude(self, *args):
        self.query = self.query.without(*args)
        return self

    async def watch(self, full_change_obj=False):
        for change in self.query.changes().run():
            yield self._wrap(change["new_val"])


class __MetaModel(models.ModelBase):
    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        setattr(cls, 'objects', ObjectHandler(cls))
        return cls


class Model(models.Model, metaclass=__MetaModel):
    schema = None

    def validate(self):
        pass

    def __json__(self):
        return self.fields.as_dict()

