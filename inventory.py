import csv
import re


class Item():

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def save_items(self,Item):
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
                return items
        except FileNotFoundError:
            print("No Inventory file found.")
    
    def create_item():
        ...

    def add_item():
        ...
    
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

    def __str__(self):
        return f'Name : {self.name}, Price: {self.price}, Quantity: {self.quantity}' 


def main():

   # Get item details from user
    name = input("Name : ")
    price = input("Price : ")
    quantity = input("Quantity : ")

    item = Item(name,price,quantity)
    print(item)
    
     

if __name__ == "__main__":
    main()