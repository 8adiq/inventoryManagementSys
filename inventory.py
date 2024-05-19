import csv
import re

class Inventory():


    def __init__(self):
        self.inventory = {} # initialization of main inventory dictionary
        self.filename = 'items.csv'

    def save_items(self):
            with open(self.filename, 'w') as file:
                writer = csv.DictWriter(file,fieldnames=['Name','Price','Quantity'])
                if file.tell() == 0: # makes sure the file is empty before creating the header row
                    writer.writeheader() # creating header row
                for item in self.inventory.values(): 
                    writer.writerow({'Name':item['Name'],'Price':item['Price'],'Quantity':item['Quantity']})

    def load_items(self):
        try:
            with open(self.filename,'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.inventory[row['Name']] = {'Name':row['Name'], 'Price':row['Price'], 'Quantity':row['Quantity']}
        except FileNotFoundError:
            print("No Inventory file found.")
        

    def add_item(self,name,price,quantity):
        """function for adding a new item to inventory"""
        if not self.get_valid_name(name) or not self.get_valid_number(price) or not self.get_valid_number(quantity):
            print("Invalid input. Please check name, price and quantity.")
            return

        self.inventory[name] = {'Name':name,'Price':price,'Quantity':quantity}
        print(f'{name} added')
        self.save_items()

    
    def find_item(self,item_to_find):
        """function for finding a particular item in the inventory"""
        found_item = self.inventory.get(item_to_find) 
        if found_item:
            print(f" Name: {found_item['Name']}")
            print(f" Price: ${found_item['Price']}")
            print(f" Quantity: {found_item['Quantity']}")
        else:
            print("There is no item with the name {item_to_find}")

    def update_item(self,name, price=None,quantity=None):
        """updating properties of a particulat item"""
        found_item = self.inventory.get(name)
        if found_item:
            ...
            if price and quantity:
                ...
                found_item['Price'] = price
                found_item['Quantity'] = quantity
                print(f" {name}'s quantity has been updated to {quantity}")
                print(f" {name}'s price has been updated to {price}")        
            elif quantity:
                ...
                found_item['Quantity'] = quantity
                print(f" {name}'s quantity has been updated to {quantity}")
            elif price:
             ...
             found_item['Price'] = price
             print(f" {name}'s price has been updated to {price}")
        else:
            print(f" There is no item named {name}")
            return
        
        self.save_items()
    
    def delete_item(self,name):
        """deleting an item from the inventory"""
        found_item = self.inventory.get(name)
        if found_item:
            del self.inventory[name]
            self.save_items()
            print(f"{name} has been deleted")
       

    def show_all_item(self):
        """showing all items in the inventory"""
        if self.inventory:
            print("*"*10,"List of items","*"*10)
            print(" Name       Price   Quantity")
            for item_name,item_data in self.inventory.items():
                print(f" {item_name:<10} ${item_data['Price']:<7} {item_data['Quantity']:<15}")
        else:
            print("Inventory is currently empty. Add a new item.")


    def purchase_item(self,item_to_buy,quant_bought):
        """adjusting stock after a purchase"""
        self.load_items()
        print(f"searching for {item_to_buy}")
        found_item = self.inventory.get(item_to_buy)
        print("Item found.")

        if quant_bought <= int(found_item['Quantity']):
            cost = int(found_item['Price']) * quant_bought
            found_item['Quantity'] = int(found_item['Quantity']) - quant_bought
            print(f"Item : {item_to_buy}")
            print(f'Quantity : ${quant_bought}')
            print(f"Your total cost would be ${cost}")
        else:
            print(f"Sorry we only have {found_item['Quantity']} {item_to_buy} left in stock")
        self.save_items()
        

    def return_item(self,item_to_return,quant_to_return):
        """adjusting stock after an item has been returned"""
        found_item = self.inventory.get(item_to_return)
        refund = int(found_item['Price']) * quant_to_return
        found_item['Quantity'] = int(found_item['Quantity']) + quant_to_return
        print(f"An amount of ${refund} would be refunded to you.")
        self.save_items()

    def get_valid_number(self,value):
        ...
        pattern = r"^[+]?[0-9]*(\.[0-9]+)?$"
        return  re.match(pattern, str(value)) is not None

    def get_valid_name(self,name):
        ...
        pattern = r"^[a-zA-Z _]+$"
        return re.match(pattern,name) is not None
        

    def get_valid_choice(self,min_value,max_value):
        ...
        while True:
            choice = int(input(f"Enter your choice {min_value}-{max_value}  "))
            try:
                if min_value <= choice <= max_value:
                    return choice
                else:
                    print(f" Invalid choice. Enter a value between {min_value} and {max_value}")
            except ValueError:
                print("Invalid input. Enter a valid number. ")


    def __str__(self):
        return f'Name : {self.name}, Price: {self.price}, Quantity: {self.quantity}' 



def main():
    """ main function that interacts with the user for inputs """

    inventory = Inventory() #laoding an instance of the inventory class
    inventory.load_items()  #loading all items in the inventory

    print('\nChoose an option')
    print('1. Business Owner')
    print('2. Customer')
    print('3. Exit Program')

    first_choice = int(inventory.get_valid_choice(1,3))

    if first_choice == 1:

        print('\nChoose any option')
        print('1. Add an item')
        print('2. Find an item')
        print('3. Update an item')
        print('4. Show all items')
        print('5. Delete an item')
        print('6. Exit program')

        choice = int(inventory.get_valid_choice(1,6))

        if choice == 1:
            ...
            name = input("Name : ")
            price = float(input("Price : "))
            quantity = int(input("Quantity : "))

            inventory.add_item(name,price,quantity)
            
        elif choice == 2:
            ...
            item_to_find = input("Please enter the name of the item you are looking for ")
            inventory.find_item(item_to_find)

        elif choice == 3:
            ...
            inventory.show_all_item()
            item_to_update = input("Please enter the name of the item you wish to update ")

            if item_to_update:
                print("\nChoose an option")
                print("1. Price")
                print("2. Quantity")
                print("3. Both")

                property_to_update = int(input("Choose what you would like to update "))

                if property_to_update == 1:
                    ...
                    new_price = input("Please enter the new price ")
                    inventory.update_item(item_to_update,price=new_price)
                elif property_to_update == 2:
                    ...
                    new_quantity = input("Please enter the new quantity ")
                    inventory.update_item(item_to_update,quantity=new_quantity)
                elif property_to_update == 3:
                    new_price = input("Please enter the new price")
                    new_quantity = input("Please enter the new quantity")
                    inventory.update_item(item_to_update,new_price,new_quantity)
                else:
                    print("Select the correct options")

            else:
                print("Please enter the name of then item you wish to update ")
        
        elif choice == 4:
            ...
            inventory.show_all_item()

        elif choice == 5:
            ...
            inventory.show_all_item()
            item_to_delete = input("Enter the name of the item you wish to delete ")
            inventory.delete_item(item_to_delete)

        elif choice == 6:
            inventory.save_items()
            print("Exiting the Inventory")
            exit()
        else:
            print("Invalid input. Enter the correct input")
    
        
    elif first_choice == 2:
        ...

        while True:

                    print("\nChoose an option")
                    print("1. Purchase an item")
                    print("2. Return an item")
                    print("3. Exit program")
                    choice = int(inventory.get_valid_choice(1,3))

                    if choice == 1:
                        ...
                        inventory.show_all_item()
                        item_to_buy = input("Please enter the name of the item you wish to buy ")
                        quant_to_buy = int(input("Please enter the quantity you wish  to buy "))
                        inventory.purchase_item(item_to_buy,quant_to_buy)
                    elif choice == 2:
                        ...
                        item_to_return = input("Please enter the name of the item you are returning ")
                        quant_to_return = int(input("Please enter the quantity "))
                        inventory.return_item(item_to_return,quant_to_return)

                    elif choice == 3:
                        ...
                        inventory.save_items()
                        print("Exiting the Inventory")
                        exit()
                    else:
                        ...
                        print("Invalid input. Enter the correct option")
    else:
        inventory.save_items()
        print("Exiting the Inventory")
        exit()
   
    
     

if __name__ == "__main__":
    main()