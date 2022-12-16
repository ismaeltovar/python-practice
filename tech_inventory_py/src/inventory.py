import json
from json.decoder import JSONDecodeError

inventory = {}
inv_items = 0
org_name = "anonymous"
item_props = ["price", "rating", "sales"]
# Scale rating system is from 1-5 stars
rating_scale = list(range(1, 6))


def count():
    """Print number of items in inventory."""
    print(f"Number of items: {inv_items}")


def items():
    """Return name of each item in inventory, as a list."""
    return inventory.keys()


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


def add(items):
    """Add items to inventory.
    
    Adds all of the items passed to the function to the inventory.

    Keyword arguments:
    **item -- dictionary of items to add.

    Each item should be in the format of keyword={prop_name: prop_value, ...} 

    *DOES NOT validate if the item is already in the dictionary.
    """
    try:
        new_inv = inventory
    except UnboundLocalError:
        new_inv = {}
    for item, props in items:
        new_inv[item] = props
        inv_items += 1
    inventory = new_inv

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(new_inv, f, indent="4")
    print(f"{inv_items} items stocked.")
