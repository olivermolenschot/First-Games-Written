#Just write the same function in the child class, it will override the parent function
class Animal:
    def eat(self):
        print('This dog loves to eat')

class Rabbit(Animal):
    def eat(self):
        print('This rabbit loves to eat')
ravioli = Rabbit()
ravioli.eat()