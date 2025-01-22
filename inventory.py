import time


def main_menu():
    done = False
    print("**********Inventory management system**********")
    Inventory = []
    print("Please choose from the following options (1-3): ")
    time.sleep(2)
    print("1. Display Inventory")
    time.sleep(2)
    print("2. Add Inventory")
    time.sleep(2)
    print("3. Exit")

    while done==False:
        choice = int(input(""))
        if choice == 1:
            print(Inventory)
        elif choice == 2:
            item = input("What would you like to add?")
            Inventory.append(item)
            print(Inventory)
        elif choice == 3:
            done = True
            quit()


main_menu()