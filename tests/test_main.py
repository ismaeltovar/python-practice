import pytest

from src import menu
from src.inventory import Inventory

class TestMain():
    inv = Inventory(data_file="tests/test_data.json")

    def test_inv_instance(self):
        # "non-empty inventory before load is called"
        assert self.inv == {}