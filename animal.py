class Animal:
    def __init__(self, eats, sounds):
        self.sounds = sounds
        self.eats = eats

    def eat(self):
        return self.eats

    def sound(self):
        return self.sounds

dog = Animal("Food", "Bark")
cat = Animal("Food", "Meows")
