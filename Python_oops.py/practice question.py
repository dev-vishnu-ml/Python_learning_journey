class shoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,item_name,price):
        item = {"item_name: ": item_name ,"price": price}
        self.items.append(item)
        print(f"added name: {item_name} and price: {price} to the cart")

    def remove_item(self,item_name):
        found = False
        for item in self.items:
            if item["name"].lower() == item_name.lower():
                self.items.remove(item)
                print(f"remove this item {item_name} to this cart")
                found = True
                break
            if not found:
                print(f" this item {item_name} doesn't exist in this cart")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

cart1 = shoppingCart()
cart1.add_item("laptop",50000)
cart1.add_item("mouse",500)
cart1.add_item("keyboard",1500)

print(cart1.calculate_total())