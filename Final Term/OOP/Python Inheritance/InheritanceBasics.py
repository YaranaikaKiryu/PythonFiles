class Animal:
    def __init__(self,name):
        self.name = name
    
    def speaks(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"
    
dog = Dog("Sam")
cat = Cat("Mew")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")