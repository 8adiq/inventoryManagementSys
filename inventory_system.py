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
        else:
            print("There is no item with the name {name_to_find}")

    @staticmethod
    def update_item(name_to_update, item_list):
        """Function to update the details of an item"""
        item_to_update = None
        for item in item_list:
            if item["Name"].lower() == name_to_update.lower():
                item_to_update = item
            break
        if item_to_update:
            print("\nChoose an what you want to update")
            print("1. Quantity")
            print("2. Price")

            quantity_or_price = int(input("What item do you wish to update  "))

            if quantity_or_price == 1:
                new_quantity = int(input("Enter the new quantity  "))
                item_to_update["Quantity"] = new_quantity
                print("Quantity successfully updated")
                # show updated item

            else:
                new_price = int(input("Enter the new price  "))
                item_to_update["Price"] = new_price
                print("Price successfully added")
                # Show updated item
        save_items(item_list)

    @staticmethod
    def delete_item(index, item_list):
        """Function to delete an item"""

        if 0 <= index < len(item_list):
            del item_list[index]
            print("Item has been deleted")
        else:
            print("Invalid index. No Item has been deleted")
        
        save_items(items_list)
        print("\nItem list")
        for i, items in enumerate(item_list):
            print(f"{i+1} : {items["Name"]}")

    @staticmethod
    def after_purchase(item_list):
        """Function to adjust the quantity after a sale has been made"""

        name = str(input("Enter the name of the item  "))
        quantity = int(input("Enter the quantity of the item  "))

        for item in item_list:
               if item['Name'].lower() == name.lower():
                item["Quantity"] -= quantity
        print("Item purchased")
        save_items(item_list)

    @staticmethod
    def return_item(item_list):
        """Function to adjust the quantity of a item after a return"""

        name = str(input("Enter the name of the item  "))
        quantity = int(input("Enter the quantity of the item  "))

        for item in item_list:
            if item["Name"].lower() == name.lower():
                item['Quantity'] += quantity
        print("Item Returned")
        save_items(item_list)


# First User interaction
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
        name_to_find = str(input("Enter the name of the item you are looking for  "))

        Item.find_item(name_to_find, items_list)
    elif choice == 3:
        name_to_update = str(input("Enter the name of the item you want to update  "))

        Item.update_item(name_to_update, items_list)

    elif choice == 4:
        print("\nItem list")
        for i, items in enumerate(items_list):
            print(f"{i+1} : {items["Name"]}")

        index_to_delete = input("Enter the index of the item you want to delete  ")

        if index_to_delete.isdigit():
            index_to_delete = int(index_to_delete) -1
            Item.delete_item(index_to_delete,items_list)

    else:
        print("\nchoose an option")
        print("1. Business Owner")
        print("2. Customer")
        print("3. Exit program")

        first_choice = int(input("Are you a Business Owner or a Customer  "))



else:
    print("\nchoose an option")
    print("1. Purchase an item")
    print("2. Return an item")
    print("3. Back")

    choice = int(input("Enter option 1,2 or 3  "))

    if choice == 1:
        # Purchasing an item

        Item.after_purchase(items_list)

    elif choice == 2:
        print("Return an item")

        Item.return_item(items_list)

    else:
        print("\nchoose an option")
        print("1. Business Owner")
        print("2. Customer")
        print("3. Exit program")

        first_choice = int(input("Are you a Business Owner or a Customer  "))

