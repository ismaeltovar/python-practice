import pytest
import json

from src.inventory import Inventory

# May be used in the future
# @pytest.fixture
# def generate_item():
#     name = "item"
#     price = 100
#     rating = 5
#     sales = 1000
#     return {name: {"price": price, "rating": rating, "sales": sales}}


class TestInventory():
    inv = Inventory(data_file="tests/data.json")
    add_item = {"item": {"price": 100, "rating": 5, "sales": 100}}

    @pytest.mark.skip("Not implemented yet")
    def tearDown(self):
        # Tear down method (Not implemented)
        pass
    
    def test_load_json(self):
        """Test if JSON data is loaded correctly"""
        with open("tests/data.json", "r", encoding="utf-8") as f:
            json_read = json.load(f)
            self.inv.load()
            #  "JSON not loaded properly"
            assert self.inv.inventory == json_read

    def test_inv_items_counter(self):
        """Tests if the inv_items counter is working properly"""
        inv_len = len(self.inv.inventory)
        items_count = self.inv.inv_items
        #  "inv_items counter not accurate")
        assert inv_len == items_count

    def test_add(self):
        """Test if add function adds an element"""
        begin_len = self.inv.inv_items
        self.inv.add(items=self.add_item)
        # check if item is in inventory
        assert "item", self.add_item.get("item") in self.inv.inventory
        # check if inv_items is incrementing correctly
        assert begin_len + 1 == self.inv.inv_items
        # Check if new item is loaded to JSON file
        with open(self.inv.data_file, "r", encoding="utf-8") as f:
            json_read = json.load(f)
            # Check if items are in JSON file
            assert "item", self.add_item.get("item") in json_read