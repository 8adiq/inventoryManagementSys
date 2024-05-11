import csv
import re


class Item():
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        # self.save_items()

    def save_items(self):
            with open('items.csv', 'a') as file:
                writer = csv.DictWriter(file,fieldnames=['Name','Price','Quantity'])
                writer.writerow=({'Name':self.name,'Price':self.price,'Quantity':self.quantity})

    def load_items(self):
        items = []
        try:
            with open('items.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    items.append({'Name':row['Name'], 'Price':row['Price'], 'Quantity':row['Quantity']})
        except FileNotFoundError:
            print("No Inventory file found.")
        return items
    
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


class Inventory():
    
    items = []

    def add_item(cls,item):
        item = Item()
        cls.items.append(item)
        item.save_items()
    
    def find_item():
        ...

    def update_item():
        ...
    
    def delete_item():
        ...

    def show_all_item():
        ...

    def purchase_item():
        ...

    def return_item():
        ...

    



def main():

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
            item = Item(name,price,quantity)
            print(item)
            
        elif choice == 2:
            ...

        elif choice == 3:
            ...
        
        elif choice == 4:
            ...

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