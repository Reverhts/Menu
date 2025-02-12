import time

class InventorySystem:
    def __init__(self):
        self.inventory = []
    
    def display_inventory(self):
        print("Current Inventory: ", self.inventory)
    
    def add_inventory(self, item):
        self.inventory.append(item)
        print(f'Item "{item}" added to inventory.')
    
    def main_menu(self):
        done = False
        print("**********Inventory Management System**********")
        
        while not done:
            print("\nPlease choose from the following options (1-3): ")
            time.sleep(0.5)
            print("1. Display Inventory")
            time.sleep(0.5)
            print("2. Add Inventory")
            time.sleep(0.5)
            print("3. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.display_inventory()
            elif choice == 2:
                item = input("What would you like to add? ")
                self.add_inventory(item)
            elif choice == 3:
                print("Exiting system.")
                done = True
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    system = InventorySystem()
    system.main_menu()