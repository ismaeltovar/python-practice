import pytest
import json

from src.main import main
from src.inventory import Inventory

class TestMain():
    data_file = "tests/data.json"
    inv = Inventory(data_file=data_file)

    def test_inv_instance(self):
        """Check if inventory is empty when first creating an Inventory object."""
        # "non-empty inventory before load is called"
        assert self.inv.inventory == {}

    @pytest.mark.skip("Not yet implemented.")
    def test_inv_load(self):
        """Check if main inventory object is loading properly."""
        main()
        self.inv.load()
        assert main.inv.inventory == self.inv.inventory