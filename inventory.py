import csv
import re

class Inventory():


    def __init__(self):
        self.inventory = {}
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
        ...
        self.inventory[name] = {'Name':name,'Price':price,'Quantity':quantity}
        print(f'{name} added')
        self.save_items()

    
    def find_item(self,item_to_find):
        ...
        found_item = self.inventory.get(item_to_find) 
        if found_item:
            print(f" Name: {found_item['Name']}")
            print(f" Price: ${found_item['Price']}")
            print(f" Quantity: {found_item['Quantity']}")
        else:
            print("There is no item with the name {item_to_find}")

    def update_item(self,name, price=None,quantity=None):
        ...
        self.show_all_item()
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
        ...
        found_item = self.inventory.get(name)
        if found_item:
            del self.inventory[name]
            self.save_items()
            print(f"{name} has been deleted")
       

    def show_all_item(self):

        if self.inventory:
            print("*"*10,"List of items","*"*10)
            print(" Name       Price   Quantity")
            for item_name,item_data in self.inventory.items():
                print(f" {item_name:<10} ${item_data['Price']:<7} {item_data['Quantity']:<15}")
        else:
            print("Inventory is currently empty. Add a new item.")


    def purchase_item(self,item_to_buy,quant_bought):
        ...
        found_item = self.inventory.get(item_to_buy)

        if quant_bought <= int(found_item['Quantity']):
            cost = int(found_item['Price']) * quant_bought
            found_item['Quantity'] = int(found_item['Quantity']) - quant_bought
            print(f" Your total cost would be ${cost}")
        else:
            print("We do not have that amount, please lower your quantity")
        self.save_items()
        

    def return_item():
        ...


    def change_price():
        ...

    def __str__(self):
        return f'Name : {self.name}, Price: {self.price}, Quantity: {self.quantity}' 



def main():

    inventory = Inventory()
    inventory.load_items()

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
                print("Please enter the name of then item you wish to update")
        
        elif choice == 4:
            ...
            inventory.show_all_item()

        elif choice == 5:
            ...
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
            customer_name = input("What is your name ? ")
            
            if customer_name:
                while True:
                    print("\nChoose an option")
                    print("1. Purchase an item")
                    print("2. Return an item")
                    print("3. Exit program")
                    choice = int(input(f"Hello {customer_name}, what do you wish to do ? "))

                    if choice == 1:
                        ...
                        item_to_buy = input("Please enter the name of the item you wish to buy")
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
                        continue
            else:
                print("Name cannot be empty")
                continue
    else:
        inventory.save_items()
        print("Exiting the Inventory")
        exit()
   
    
     

if __name__ == "__main__":
    main()