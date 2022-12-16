import inventory
from inventory import item_props, rating_scale, org_name
import console


def display():
    """Print Main menu with options
    
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
            console.invalid_in()
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
    """Print prompt to add items to inventory."""
    items = {}
    valid_in = False
    first_iteration = True
    while valid_in is False:
        console.clear()
        if first_iteration is False:
            console.invalid_in()
        try:
            print("Number of items to add", end='')
            count = int(input(": "))
        except ValueError:
            if first_iteration is True:
                first_iteration = True
            continue
        else:
            for i in range(1, count + 1):
                # Does not exit loop until valid name is found
                valid_in = False
                while valid_in is False:
                    print(f"Item #{i}", end='')
                    name = input(": ")
                    if name in inventory.items():
                        console.invalid_in("name: already in inventory")
                        continue
                    valid_in = True
                # Prompts for each prop of each item name entered
                props = {}
                p_indx = 1
                while p_indx < len(item_props):
                    append_txt = ""
                    cur_prop = item_props[p_indx]
                    if cur_prop == "price":
                        # Price prop
                        append_txt = " (in $)"
                    elif cur_prop == "rating":
                        # Rating prop
                        append_txt = " (out of 5)"
                    try:
                        print(f"{cur_prop}{append_txt}", end='')
                        cli_in = int(input(": "))
                    except ValueError:
                        console.invalid_in()
                        continue
                    else:
                        if (cli_in not in rating_scale  
                            and cur_prop == "rating"):
                            console.invalid_in("rating")
                            continue
                    props[cur_prop] = cli_in
                    p_indx += 1
                # Adds props taken from input in loop to name
                items[name] = props
                
            inventory.add(items)
            console.enter_pmt()


def view_inventory():
    console.clear()
    inventory.view()
    console.enter_pmt()