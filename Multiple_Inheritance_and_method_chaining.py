class Dog:
    def eat(self):
        print('He loves to eat')
        return self
class Fat:
    def overweight(self):
        print('He ate too much')
        return self
class Pet(Dog,Fat):
    pass


Luki = Pet ()

Fat.overweight(Luki)
Luki.overweight()
print('---------------------')
Luki.overweight().eat().eat()