inventory = {}


def view():
    """View current inventory."""
    for item, props in inventory:
        print(f"{item}:  ")
        for prop, val in props:
            print(f"{prop} = {val}\n")
        print("\n")


def add(**items):
    """Add items to inventory.
    
    Adds all of the items passed to the function to the inventory.
    Keyword arguments:
    **item -- dictionary of items to add.
    Each item should be in the format of keyword={prop_name: prop_value, ...} 
    """
    new_inv = {}
    for name, props in items:
        new_inv[name] = props
    inventory = new_inv