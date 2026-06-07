class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        print(f"{self.name} says {self.sound}")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")
    def speak(self):
        print(f"{self.name} says Woof") 
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")
    def speak(self):
        print(f"{self.name} says Meow")
dog = Dog("Buddy")
cat = Cat("Kitty")
dog.speak()
cat.speak()