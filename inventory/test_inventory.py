from inventory import Inventory
from product import Product
import pytest


@pytest.fixture
def inv():
    return Inventory()


@pytest.fixture
def prodct():
    return Product("Default", 10.5, 5)


def test_add_or_get_product(inv, prodct):
    inv.add_product(prodct)
    assert prodct in inv


def test_del_product(inv, prodct):
    inv.add_product(prodct)
    assert prodct in inv
    del inv[0]
    assert (prodct in inv) is False


def test_total(inv, prodct):
    inv.add_product(prodct)
    inv.add_product(prodct)
    assert inv.total() == 21.0


def test_add_item_other_than_product(inv):
    with pytest.raises(AttributeError):
        inv.add_product("A")
        inv.add_product(1)
