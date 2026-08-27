# basically two type of polymorphism in python 1.function overriding 2.Duck Typing
class Dog:
    def speak(self):
        print("bark")

class Cow:
    def speak(self):
        print("Moo!")

class Robot:
    def speak(self):
        print("Beep Boop")

def make_it_speak(entity):
    entity.speak()

d = Dog()
c = Cow()
r = Robot()

for e in [d,c,r]:
    make_it_speak(e)