class FieldError(Exception): pass
class FieldRequired(FieldError): pass

class Field(object):
    def __init__(self, pk=False, required=False, hidden=False):
        self.pk = pk
        self.required = required
        self.hidden = hidden

    def treat(self, data):
        return data

    def validate(self, data):
        if self.required and data is None:
            raise FieldRequired()
        return data

class PasswordField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{"hidden": True, **kwargs})

