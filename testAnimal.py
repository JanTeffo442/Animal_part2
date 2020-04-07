import unittest
from animal import Animal
from cat import Cat

class AnimalTests(unittest.TestCase):

    def setUp(self):
        self.cat1 = Animal('Food', 'Meow')
        self.dog1 = Animal('Food', 'Bark')
 
    def test_dog_sound(self):
        print('test_dog_sound Passed')
        self.assertEqual(self.dog1.sounds, 'Bark')
        
    def test_dog_eats(self):
        print('test_dog_eats Passed')
        self.assertEqual(self.dog1.eats, 'Food')

    def test_cat_sound(self):
        print('test_cat_sound Passed')
        self.assertEqual(self.cat1.sounds, 'Meow')

    def test_cat_eats(self):
        print('test_cat_eats Passed')
        self.assertEqual(self.cat1.eats, 'Food')

if __name__ == "__main__":
    unittest.main()
