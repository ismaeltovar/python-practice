import inventory
from inventory import item_props, org_name
import console


def display():
    """Prints Main menu with options
    
    Prints Menu and prompts user to enter an option. 
    Does not exit loop until user enters a valid option.

    Return value:
    cli_in -- valid user option
    """
    menu_ops = [1, 2, 3]
    valid_in = False
    first_iteration = True
    while valid_in is False:
        console.clear()
        print(f"Welcome to {org_name}'s technology inventory.\n")
        if first_iteration is False:
            print("***Invalid input***")
        print("Menu:\n1. Add items\n2. View inventory\n3. Exit")
        try:
            cli_in = int(input("> "))
        except ValueError:
            if first_iteration is True:
                first_iteration = False
            continue
        else:
            valid_in = True
    return int(cli_in)


def add_inventory():
    console.clear()
    items = {}
    print("Number of items to add", end='')
    count = input(": ")
    for i in range(1, count + 1):
        print(f"Item #{i}", end='')
        name = input(": ")
        props = {}
        for prop in item_props:
            print(f"{prop}")
            props[prop] = input(": ")
        items[name] = props
    inventory.add(items)
    console.enter_pmt()


def view_inventory():
    console.clear()
    inventory.view()
    console.enter_pmt()