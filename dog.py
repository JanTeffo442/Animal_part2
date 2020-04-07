from animal import Animal
class Dog(Animal):

    def __init__(self, eats, animal_sound):
        super().__init__(eats, animal_sound)

    def eat(self):
        return 'Rax eats'
    
    def sound(self):
        return 'Dog barks'

dog1 = Dog("Food", "Bark")

print(dog1.eat())
print(dog1.sound())