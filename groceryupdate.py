#Still working on it..made changes to reflect review today.

stores = [] 
test = []
class StoreList:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []

class Item: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price 

while True:

    print("1. Add Shopping List: ")
    print("2. View All Shopping List: ")
    print("3. Add Item to a Shopping List: ")
    print("4. Delete store")
    print("5. Delete Item")
    print("q: Quit: ")

    choice = input("Enter a selection: ")

    if choice == "q":
        break
    
    elif choice == "1":
        store_name = input("Add store: ")
        store_address = input("Add address: ")
        grocery_list = StoreList(store_name, store_address)
        stores.append(grocery_list)
    
    elif choice == "2": 
        for store in stores: 
            print(store.name)
        
            for item in store.items: 
                print(item.name)

    elif choice == "3": 
        
        for index in range(0, len(stores)): 
            store = stores[index]
            print(f"{index + 1}. {store.name}")
        
        store_number = int(input("Enter Store Number: "))
        store = stores[store_number - 1]
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: ")) 
        item = Item(item_name, item_price)
        store.items.append(item)

    elif choice == "4":
        for index in range(0, len(stores)):
            print(f"{index + 1}. {store.name}")
            store = stores[index]
        store_number = int(input("Enter Store Number: "))
<<<<<<< HEAD
        del stores[store_number - 1]

    elif choice == "5":
        #

        
=======
        store = stores[store_number - 1]
        store_to_delete = int(input("What is the store you would like to delete")
>>>>>>> 986b9c00878c3e1f582d07668045a7652a1d5af2
