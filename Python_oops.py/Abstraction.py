# abstraction is hiding internal details and showing only functionality/(essential features).
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def Make_sound(self):
        pass

class Lion(Animal):
    def Make_sound(self):
        print("Roar!")

class Cat(Animal):
    def Make_sound(self):
        print("Meow!")

class Cow(Animal):
    def Make_sound(self):
        print("Moo!")

lion = Lion()
lion.Make_sound()

cat = Cat()
cat.Make_sound()

cow = Cow()
cow.Make_sound()

