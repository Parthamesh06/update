class Animal():
    def speak(self):
        return "Animal say ..."

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
animal=Animal()
print(cat.speak())
print(dog.speak())
print(animal.speak())