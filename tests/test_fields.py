from brink import fields
import pytest

def test_field_treat():
    field = fields.Field()
    assert field.validate("val") == "val"

def test_field_validate_required():
    field = fields.Field(required=True)

    with pytest.raises(fields.FieldRequired):
        field.validate(None)

    assert field.validate("val") == "val"

def test_integer_field_validate_type():
    field = fields.IntegerField()

    with pytest.raises(fields.FieldInvalidType):
        field.validate("test")

    assert field.validate(10) == 10

def test_char_field_validate_min_length():
    field = fields.CharField(min_length=5)

    with pytest.raises(fields.FieldInvalidLength):
        field.validate("test")

    assert field.validate("testing") == "testing"

def test_char_field_validate_max_length():
    field = fields.CharField(max_length=5)

    with pytest.raises(fields.FieldInvalidLength):
        field.validate("testing")

    assert field.validate("test") == "test"

def test_char_field_validate_type():
    field = fields.CharField()

    with pytest.raises(fields.FieldInvalidType):
        field.validate(10)

    assert field.validate("test") == "test"

def test_bool_field_validate_type():
    field = fields.BooleanField()

    with pytest.raises(fields.FieldInvalidType):
        field.validate("test")

    assert field.validate(True)
    assert not field.validate(False)

def test_list_field_validate_subtype():
    field = fields.ListField(fields.CharField())

    with pytest.raises(fields.FieldInvalidType):
        field.append(1)

    field.append("test1")
    field.append("test2")
    assert len(field) == 2

def test_list_field_pop():
    field = fields.ListField(fields.IntegerField())
    field.append(1)
    field.append(2)
    field.append(3)

    assert len(field) == 3
    assert field.pop() == 3
    assert len(field) == 2

def test_list_field_validate_subvalidation():
    field = fields.ListField(fields.CharField(min_length=5))

    with pytest.raises(fields.FieldInvalidLength):
        field.append("test")

    field.append("testing")
    assert len(field) == 1
    assert field.pop() == "testing"
