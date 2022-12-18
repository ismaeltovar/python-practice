import console
from menu import Menu
from inventory import Inventory


def main():
    exit = False
    inv = Inventory()
    inv.load()
    menu = Menu(inv)

    while not exit:
        selection = menu.display()
        match selection:
            case 1:
                # Add item/s to inventory
                menu.add_inventory()                
            case 2:
                # View inventory
                menu.view_inventory()
            case 3:
                console.clear()
                exit = True
            case _:
                print("Invalid option.")


if __name__ == "__main__":
    main()