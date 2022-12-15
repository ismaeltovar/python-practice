import menu
import inventory
import console


def main():
    exit = False
    inventory.load()

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