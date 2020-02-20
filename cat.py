from animal import Animal
class Cat(Animal):
    def __init__(self, eats, sounds):
        super().__init__(eats, sounds)

    def eat(self):
        #print(self.name + " eats")
        return self.eats
    
    def sound(self):
        #print(self.sounds + " meow")
        return self.sounds

cat1 = Cat("Food", "Meow")
cat1.eat()
cat1.sound()