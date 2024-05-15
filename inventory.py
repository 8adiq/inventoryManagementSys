import csv
import re


# items = []
class Inventory():


    def __init__(self):
        self.inventory = {}
        self.filename = 'items.csv'

    def save_items(self):
            with open(self.filename, 'a') as file:
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
        ...
        self.inventory[name] = {'Name':name,'Price':price,'Quantity':quantity}
        print(f'{name} added')
        self.save_items()
        print(self.inventory)

    
    def find_item(self,item_to_find):
        self.load_items()
        ...
        found_item = self.inventory.get(item_to_find) 
        if found_item:
            print(f" Name: {found_item['Name']}")
            print(f" Price: {found_item['Price']}")
            print(f" Quantity: {found_item['Quantity']}")
        else:
            print("There is no item with the name {item_to_find}")

    def update_item(self,name, price="", quantity=""):
        self.load_items()
        ...
        if price:
            ...
            for item in items:
                if item['Name'] == name:
                    item['Price'] = price            
        else:
            ...
            for item in items:
                if item['Name'] == name:
                    item['Quantity'] = quantity
    
    def delete_item(self,name):
        self.load_items()
        ...
        if name:
            for item in items:
                if item['Name'] == name:
                    # items.pop(item['Name'])
                    # print(item)
                    print(self.inventory)
                    break
                else:
                    print(f"No item named {name}")
        else:
            print("Name can not be empty")
        self.save_items()


    def show_all_item(self):
        self.load_items()

        if self.inventory:
            print("*"*10,"List of items","*"*10)
            print("Name      Price     Quantity")
            print(self.inventory)
            for item in self.inventory:
                # print(f"{item['Name']}      {item['Price']}      {item['Quantity']}")
                print(item)

        else:
            print("Inventory is currently empty. Add a new item.")


    def purchase_item():
        ...

    def return_item():
        ...

    
    def after_purchase(self,amt_bought):
        if amt_bought <= self.quantity:
            self.quantity -= amt_bought
            print(f'You have {self.quantity} of {self.name} left')
        else:
            print(f'There are not enough {self.name}')

    def after_return():
        ...

    def change_price():
        ...

    def __str__(self):
        return f'Name : {self.name}, Price: {self.price}, Quantity: {self.quantity}' 



def main():

    inventory = Inventory()
    # inventory.load_items()

    print('\nChoose an option')
    print('1. Business Owner')
    print('2. Customer')
    print('3. Exit Program')

    first_choice = int(input('Proceed as a Business Owner or Customer '))

    if first_choice == 1:

        print('\nChoose any option')
        print('1. Add an item')
        print('2. Find an item')
        print('3. Update an item')
        print('4. Show all items')
        print('5. Delete an item')
        print('6. Exit program')

        choice = int(input('What do you wish to do '))

        if choice == 1:
            ...
            # Get item details from user
            name = input("Name : ")
            price = input("Price : ")
            quantity = input("Quantity : ")

            inventory.add_item(name,price,quantity)
            
        elif choice == 2:
            ...
            item_to_find = input("Please enter the name of the item you are looking for ")
            inventory.find_item(item_to_find)

        elif choice == 3:
            ...
            item_to_update = input("Please enter the name of the item you wish to update ")

            if item_to_update:
                print("\nChoose an option")
                print("1. Price")
                print("2. Quantity")

                property_to_update = int(input("Choos what you would like to update"))

                if property_to_update == 1:
                    ...
                    new_price = input("Please enter the new price ")
                    inventory.update_item(item_to_update,new_price)
                elif property_to_update == 2:
                    ...
                    new_quantity = input("Please enter the new quantity ")
                    inventory.update_item(item_to_update,new_quantity)
                else:
                    print("Select the correct options")
        
        elif choice == 4:
            ...
            inventory.show_all_item()

        elif choice == 5:
            ...
            item_to_delete = input("Enter the name of the item you wish to delete ")
            inventory.delete_item(item_to_delete)

        else:
            exit()
    
        

    elif first_choice == 2:
        ...
    else:
        exit()
   
    
     

if __name__ == "__main__":
    main()