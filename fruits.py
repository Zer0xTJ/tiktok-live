fruits = {
    "apple": 2.5,
    "orange": 2.5,
    "potato": 3.5
}


def add_items():
    x = int(input("Enter the items count: "))  # 2
    for i in range(1, x + 1):
        # get fruit nae and price from user
        fruit = input(f"{i} - Enter the fruit name: ")
        price = float(input(f"{i} - Enter the price: "))
        fruits[fruit] = price


def delete_item():
    fruit = input('Enter Fruit name to delete: ')
    del fruits[fruit]


def update_item():
    fruit = input("Enter the name of the item: ")
    price = input("Enter new price: ")
    fruits[fruit] = float(price)


def find_items_by_price():
    price = float(input("Enter the price: "))
    for item in fruits:
        if fruits[item] == price:
            print(item)


def clear_all():
    # fruits.clear()
    global fruits
    fruits = {}


while (True):
    print("[1] - Add items")
    print("[2] - Show items")
    print("[3] - delete item")
    print("[4] - update item price")
    print("[5] - find item by it's price")
    print("[6] - Clear all")
    # enter a price: 2.5
    print("[q] - quit")
    option = input("Enter you choice: ")
    if option == 'q':
        break
    elif option == '1':
        add_items()
    elif option == "2":
        print(fruits)
    elif option == "3":
        delete_item()
    elif option == '4':
        update_item()
    elif option == "5":
        find_items_by_price()
    elif option == "6":
        clear_all()
