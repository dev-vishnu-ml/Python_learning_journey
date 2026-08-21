class bank:
    def __init__(self,name,balance):
        self.name = name
        self._balance = balance #protected attributes

    def dispaly(self):
         return self._balance

acc1 = bank("rahul",10_000)
print(acc1.name,acc1.dispaly())

'''
we can access the protected attributes directely like print(acc1._balance) but it's not a 
good thing all time use the functions acces this attribute because if we acces the directely 
then end the concepet of data hiding.
'''