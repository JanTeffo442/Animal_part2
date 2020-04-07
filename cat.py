from animal import Animal

class Cat(Animal):
    def __init__(self, eats, sounds):
        super().__init__(eats, sounds)

    def eat(self):
        return 'Stormy eats'
    
    def sound(self):
        return 'cat meows'

cat1 = Cat("Food", "Meow")

print(cat1.eat())
print(cat1.sound())

