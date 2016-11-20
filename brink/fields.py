import sys

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

class FieldInvalidType(FieldError): pass

class IntegerField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, data):
        if type(data) is not int:
            raise FieldInvalidType()
        return super().validate(data)

class FieldInsufficientLength(FieldError): pass

class CharField(Field):
    def __init__(self, *args, min_length=0, max_length=sys.maxsize, **kwargs):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    def validate(self, data):
        if len(data) < self.min_length:
            raise FieldInsufficientLength()

        if len(data) > self.max_length:
            raise FieldInsufficientLength()

        return super().validate(data)

class PasswordField(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **{"hidden": True, **kwargs})

class BooleanField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, data):
        if type(data) is not bool:
            raise FieldInvalidType()
        return super().validate(data)
