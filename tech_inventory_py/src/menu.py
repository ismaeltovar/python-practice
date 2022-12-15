

def main_m():
    """Prints Main menu with options

    Prints Menu and prompts user to enter an option. 
    Does not exit loop until user enters a valid option.

    Return value:
    cli_in -- valid user option
    """
    menu_ops = [1, 2]
    print('Menu:\n1. Add items\n2. View inventory\n> ')
    while cli_in := input() not in menu_ops:
        print("Invalid input. Try again.\n")
    return cli_in


def m_add():
    print('Choose method:\n1. CLI Input\n2. Import CSV')


def m_view():
    print('Current inventory: \n(EMPTY)')

