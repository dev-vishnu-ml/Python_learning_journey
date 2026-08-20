# practice problem product store 
class product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        product.count += 1

    def get_info(self):
        print(f"name is: {self.product} and price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"count is: {cls.count}")

    @staticmethod
    def calculate_discount(price,discount):
        final_price = price -(discount*price/100)
        print(f"final price is: = {final_price}")

p1 = product("laptop",50_000)
p2 = product("phone",10_000)

product.get_count()
p1.calculate_discount(50000,10)
p1.get_info()

