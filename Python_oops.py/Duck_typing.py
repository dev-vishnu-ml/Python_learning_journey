# 2.duck typing it is the type of polymorphism
class Dog:
    def speak(self):
        print("bark")

class Cat:
    def speak(self):
        print("Meow!")

class Lion:
    def speak(self):
        print("Roar")

class Robot:
    def speak(self):
        print("beep boop")

def make_it_speak(entity):
    entity.speak()

d = Dog()
c = Cat()
l = Lion()
r = Robot()

for i in [d,c,l,r]:
    make_it_speak(i)

