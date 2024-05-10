import csv
import re


class Item():

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def save_items(self,Item):
        with open('items.csv', 'a') as file:
            writer = csv.DictWriter(file,fieldnames=['name','price','quantity'])
            writer.writerow=({'name':self.name,'price':self.price,'quantity':self.quantity})
        

    
    def load_items():
        ...
    
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


def main():

    # Get item details from user
    # name = input("Name : ")
    # price = input("Price : ")
    # quantity = input("Quantity : ")

    item = get_item_detail()
    print(item)
    

def get_item_detail():
    name = input("Name : ")
    price = input("Price : ")
    quantity = input("Quantity : ")
    return Item(name,price,quantity)
     

if __name__ == "__main__":
    main()