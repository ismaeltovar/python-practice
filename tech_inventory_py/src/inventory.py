import json
from json.decoder import JSONDecodeError

class Inventory:
    """Type to keep track of items in organization's storage."""
    inventory = {}
    inv_items = 0
    item_props = ["price", "rating", "sales"]
    # Scale rating system is from 1-5 stars
    rating_scale = list(range(1, 6))

    def __init__(self, org_name="anonymous", data_file="data.json"):
        # Saves name passed as parameter as class attribute
        self.org_name = org_name
        self.data_file = data_file

    def count(self):
        """Print number of items in inventory."""
        print(f"Number of items: {self.inv_items}")

    def items(self):
        """Return name of each item in inventory, as a list."""
        return self.inventory.keys()

    def load(self):
        """Load inventory data from json."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.inventory = json.load(f)
        except JSONDecodeError:
            print("NOTE: Inventory is empty.")
        else:
            self.count()

    def view(self):
        """View current inventory."""
        self.count()
        if self.inventory == {}:
            print("Inventory is empty.")
        else:
            for item, props in self.inventory:
                print(f"{item}:  ", end='')
                for prop, val in props:
                    print(f"{prop} = {val}")
                print("")

    def add(self, items):
        """Add items to inventory.
        
        Adds all of the items passed to the function to the inventory.

        Keyword arguments:
        **item -- dictionary of items to add.

        Each item should be in the format of keyword={prop_name: prop_value, ...} 

        *DOES NOT validate if the item is already in the dictionary.
        """
        try: 
            new_inv = self.inventory
        except UnboundLocalError:
            new_inv = {}
        for item, props in items:
            new_inv[item] = props
            self.inv_items += 1
        self.inventory = new_inv

        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(new_inv, f, indent="4")
        print(f"{self.inv_items} items stocked.")
