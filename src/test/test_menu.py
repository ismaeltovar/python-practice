import unittest
import os

from inventory import Inventory
from menu import Menu

class MenuTestCase(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory(data_file="test_data.json")
        self.menu = Menu(self.inv)

    @unittest.skip("Not implemented.")
    def test_menu_prompt(self):
        """Tests if menu prompt return right value."""
        return_val = self.menu.display()


if __name__ == "__main__":
    unittest.main()