import pytest
from marshmallow import ValidationError
from apps.usuarios.schemas import CreateUserSchema


@pytest.fixture(scope="function")
def schema():
    return CreateUserSchema()


def test_simple(schema):
    data_sample = {
        "nome": "John Doe",
        "email": "fake@test.com",
        "password": "123",
        "password2": "123"
    }
    assert schema.load(data_sample)


def test_name_size_overflow(schema):
    data_sample = {
        "nome": "John Doe"*50,
        "email": "fake@test.com",
        "password": "123",
        "password2": "123"
    }
    with pytest.raises(ValidationError, match="Longer than maximum length 256."):
        schema.load(data_sample)


def test_validate_email(schema):
    data_sample = {
        "nome": "John Doe",
        "email": "faketest.com",
        "password": "123",
        "password2": "123"
    }    
    with pytest.raises(ValidationError, match="Not a valid email address."):
       schema.load(data_sample) 
    
    data_sample["email"] = "fake@test.com"
    assert schema.load(data_sample)


def test_validate_password(schema):
    data_sample = {
        "nome": "John Doe",
        "email": "fake@test.com",
        "password": "1234",
        "password2": "123"
    }
    with pytest.raises(ValidationError, match="Passwords must be equal!"):
        schema.load(data_sample)
