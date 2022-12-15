import json
from json.decoder import JSONDecodeError

item_props = ["price", "rating", "sales"]
inventory = {}
inv_items = 0
org_name = "anonymous"


def count():
    """Print number of items in inventory."""
    print(f"Number of items: {inv_items}")


def load():
    """Load inventory data from json."""
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            inventory = json.load(f)
    except JSONDecodeError:
        print("NOTE: Inventory is empty.")
    else:
        count()


def view():
    """View current inventory."""
    count()
    if inventory == {}:
        print("Inventory is empty.")
    else:
        for item, props in inventory:
            print(f"{item}:  ", end='')
            for prop, val in props:
                print(f"{prop} = {val}")
            print("")


def add(**items):
    """Add items to inventory.
    
    Adds all of the items passed to the function to the inventory.
    Keyword arguments:
    **item -- dictionary of items to add.
    Each item should be in the format of keyword={prop_name: prop_value, ...} 
    """    
    inventory = items
    inv_items += len(items.keys())

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent="4")
    print(f"{inv_items} items stocked.")