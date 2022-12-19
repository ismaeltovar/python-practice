import pytest

from src.menu import Menu
from src.inventory import Inventory

pytest.skip("Not implemented yet.", allow_module_level=True)

class TestMenu():
    def setUp(self):
        self.inv = Inventory(data_file="test_data.json")
        self.menu = Menu(self.inv)

    # @unittest.skip("Not implemented.")
    def test_menu_prompt(self):
        """Tests if menu prompt return right value."""
        return_val = self.menu.display()