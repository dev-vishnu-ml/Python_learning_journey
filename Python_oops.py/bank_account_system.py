# bankaccount deposit money check name and balance:

class BnakAccount:
    def __init__(self,account_holder,balance):
        self.name = account_holder
        self.balance = balance

    def deposit_money(self,amount):
         self.balance  += amount
         return self.balance
    def get_balance(self):
        return self.name, self.balance
          

acc1 = BnakAccount("vishnu",5000)

print(f"Account holder name is: {acc1.name} and total balance is = {acc1.balance}")
acc1.deposit_money(5000)
print(f"updated balance is : {acc1.get_balance()}")

