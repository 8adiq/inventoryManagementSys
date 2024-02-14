"""An inventory system that does all the things listed below

# Steps
# Create item
# Add item to inventory
# Find item
# update item
# Delete item
# Purchase item and update inventory and till balance
# Return item and update inventory and till balance

"""

import json


def save_items(items):
    """Save items into a json file"""

    with open("items.json", "w", encoding="utf-8") as file:
        json.dump(items, file)


def load_items():
    """Loading saved items from a json file"""
    try:
        with open("items.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


items_list = load_items()


class Item:
    """Class for creating an item"""

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def item_details(self):
        """Function to gather the item details into a dictionary"""

        item_dict = {"Name": self.name, "Quantity": self.quantity, "Price": self.price}
        return item_dict

    @staticmethod
    def add_item(item, item_list):
        """Function to add an item to list"""

        it_details = item.item_details()
        item_list.append(it_details)
        save_items(item_list)

    @staticmethod
    def find_item(name_to_find, items_list):
        """Function to find a item"""
        found_item = None
        for item in items_list:
            if item["Name"].lower() == name_to_find.lower():
                found_item = item
            break

        if found_item:
            print("Item found")
            for key, value in found_item.items():
                print(f"{key}:  {value}")


print("\nchoose an option")
print("1. Business Owner")
print("2. Customer")
print("3. Exit program")

first_choice = int(input("Are you a Business Owner or a Customer  "))


if first_choice == 1:
    print("\nchoose an option")
    print("1. Add a new item")
    print("2. Find an item")
    print("3. Update an item")
    print("4. Delete an item")
    print("5. Back")

    choice = int(input("Enter option 1,2,3,4 or 5 to proceed  "))

    if choice == 1:

        name = str(input("Enter the name of the item  "))
        price = int(input("Enter the price of the item  "))
        quantity = int(input("Enter the quantity of the item  "))

        item = Item(name, quantity, price)

        Item.add_item(item, items_list)

    elif choice == 2:
        print("Find an item")
        name_to_find = str(input("Enter the name of the item you are looking for  "))

        Item.find_item(name_to_find, items_list)
    elif choice == 3:
        print("Update an item")

    elif choice == 4:
        print("Delete an item")

    else:
        print("\nchoose an option")
        print("1. Business Owner")
        print("2. Customer")
        print("3. Exit program")


else:
    print("\nchoose an option")
    print("1. Purchase an item")
    print("2. Return an item")
    print("3. Back")

    choice = int(input("Enter option 1,2 or 3  "))

    if choice == 1:
        print("Purchase an item")

    elif choice == 2:
        print("Return an item")

    else:
        print("\nchoose an option")
        print("1. Business Owner")
        print("2. Customer")
        print("3. Exit program")
