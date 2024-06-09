class Animal():
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return "cat meows!"
        
class Dog(Animal):
    def speak(self):
        return "Dog Barks!"

def make_sound(animal):
    animal.speak()

cat=Cat()
dog=Dog()
print(cat.speak())
print(dog.speak())
        