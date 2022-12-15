from menu import main_m, m_add, m_view


def main():
    org_name = 'company'
    exit = False
    selection = 0

    print(f'Welcome to {org_name}\'s technology inventory.\n')
    while not exit:
        selection = main_m()
        match(selection):
            case 1:
                m_add()
            case 2:
                m_view()
        exit = True


if __name__ == "__main__":
    main();