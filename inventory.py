import csv
import re
import json


items = []
class Inventory():


    def __init__(self):
        self.inventory = {}
        self.filename = 'items.csv'

    def save_items(self):
            with open(self.filename, 'a') as file:
                writer = csv.DictWriter(file,fieldnames=['Name','Price','Quantity'])
                if file.tell() == 0: # makes sure the file is empty before creating the header row
                    writer.writeheader()
                for item in self.inventory.values():
                    writer.writerow({'Name':item['Name'],'Price':item['Price'],'Quantity':item['Quantity']})

    def load_items(self):
        try:
            with open(self.filename,'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    items.append({'Name':row['Name'], 'Price':row['Price'], 'Quantity':row['Quantity']})
        except FileNotFoundError:
            print("No Inventory file found.")
        

    def add_item(self,name,price,quantity):
        ...
        self.inventory[name] = {'Name':name,'Price':price,'Quantity':quantity}
        print(f'{name} added')
        self.save_items()

    
    def find_item():
        ...

    def update_item():
        ...
    
    def delete_item():
        ...

    def show_all_item(self):
        self.load_items()

        if items:
            for item in items:
                print(f"{item['Name']} {item['Price']} {item['Quantity']}")

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

        elif choice == 3:
            ...
        
        elif choice == 4:
            ...
            inventory.show_all_item()

        elif choice == 5:
            ...

        else:
            exit()
    
        

    elif first_choice == 2:
        ...
    else:
        exit()
   
    
     

if __name__ == "__main__":
    main()