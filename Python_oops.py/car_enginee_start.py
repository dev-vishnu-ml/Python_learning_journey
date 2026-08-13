# class car:
#     def __init__(self,brand,model):
#         self.brand =brand
#         self.model =model
#         self.is_running = False

#     def start_car(self):
#         self.is_running = True
#         print("car start ho gyi")

#     def car_info(self):
#         return self.brand, self.model ,self.is_running

# my_car = car("Toyota", "Fortuner")
# my_car.start_car()
# print(f"car brand model and condition is: {my_car.car_info()}")


class shopingcart:
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.cart_items = []

    def add_item(self,items):
        for items_list in items: 
         self.cart_items.append(items_list)

    def show_cart(self):
        return self.customer_name, self.cart_items

cart1 = shopingcart("vishnu")
cart1.add_item(["shoes", "watch","socks"])
print(cart1.show_cart())















