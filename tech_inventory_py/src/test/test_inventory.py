import unittest
import json

from inventory import Inventory

class InventoryTestCase(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory(data_file="test_data.json")
        self.add_item = {"item": {"price": 100, "rating": 5, "sales": 100}}

    @unittest.skip("Not implemented.")
    def tearDown(self):
        # Tear down method (Not implemented)
        pass
    
    def test_load_json(self):
        """Test if JSON data is loaded correctly"""
        with open("test_data.json", "r", encoding="utf-8") as f:
            json_read = json.load(f)
            self.inv.load()
            self.assertEqual(self.inv.inventory, json_read, "JSON not loaded properly")

    def test_inv_items_counter(self):
        """Tests if the inv_items counter is working properly"""
        inv_len = len(self.inv.inventory)
        items_count = self.inv.inv_items
        self.assertEqual(inv_len, items_count, "inv_items counter not accurate")

    def test_add(self):
        """Test if add function adds an element"""
        begin_len = self.inv.inv_items
        self.inv.add(self.add_item)
        self.assertIn(self.add_item, self.inv.inventory, "item not in inventory")
        self.assertEqual(begin_len + 1, self.inv.inv_items, "inv_items count not incremented")
        # Check if new item is loaded to JSON file
        with open("test_data.json", "r", encoding="utf-8") as f:
            json_read = json.load(f)
            self.assertIn(self.add_item, json_read, "item not in JSON file")


if __name__ == "__main__":
    unittest.main()