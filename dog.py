from animal import Animal
class Dog(Animal):

    def __init__(self, eats, animal_sound):
        super().__init__(eats, animal_sound)

    def eat(self):
        #print(self.name + " eats")
        return self.eats
    
    def sound(self):
        #print(self.sounds + " barks")
        return self.sounds

dog1 = Dog("Food", "Bark")
dog1.eat()
dog1.sound()