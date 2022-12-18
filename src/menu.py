import console

class Menu:
    def __init__(self, inventory):
        self.inv = inventory

    def display(self, option=None):
        """Print Main menu with options
        
        Prints Menu and prompts user to enter an option. 
        Does not exit loop until user enters a valid option.

        Parameter:
        option -- menu option of selection (mainly for testing purposes)

        Return value:
        cli_in -- valid user option
        """
        menu_ops = [1, 2, 3]
        valid_in = False
        cli_in = 0
        while valid_in is False:
            print(f"Welcome to {self.inv.org_name}'s technology inventory.\n")
            print("Menu:\n1. Add items\n2. View inventory\n3. Exit")
            try:
                cli_in = int(input("> "))
            except ValueError:
                console.invalid_in()
                continue
            else:
                valid_in = True
        return cli_in


    def add_inventory(self):
        """Print prompt to add items to inventory."""
        items = {}
        valid_in = False
        while valid_in is False:
            try:
                print("Number of items to add", end='')
                count = int(input(": "))
            except ValueError:
                console.invalid_in()
                continue
            else:
                for i in range(1, count + 1):
                    # Does not exit loop until valid name is found
                    valid_in = False
                    name = ""
                    while valid_in is False:
                        print(f"Item #{i}", end='')
                        name = input(": ")
                        if name in self.inv.items():
                            console.invalid_in("name: already in inventory")
                            continue
                        valid_in = True
                    # Prompts for each prop of each item name entered
                    props = {}
                    p_indx = 1
                    while p_indx < len(self.inv.item_props):
                        append_txt = ""
                        cur_prop = self.inv.item_props[p_indx]
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
                            if (cli_in not in self.inv.rating_scale  
                                and cur_prop == "rating"):
                                console.invalid_in("rating")
                                continue
                        props[cur_prop] = cli_in
                        p_indx += 1
                    # Adds props taken from input in loop to name
                    items[name] = props
                    
                self.inv.add(items)
                console.enter_pmt()


    def view_inventory(self):
        self.inv.view()
        console.enter_pmt()