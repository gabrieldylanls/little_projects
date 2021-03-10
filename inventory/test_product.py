from product import Product
import pytest


@pytest.fixture
def default_product():
    return Product("Default", 10.5, 10)


def test_repr(default_product):
    assert repr(default_product) == "Product(name=Default, price=10.5, amount=10)"


def test_id(default_product):
    assert id(default_product) == default_product.id
