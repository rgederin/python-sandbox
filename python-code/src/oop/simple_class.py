class Dog:
    # Class attribute
    voice = "bark bark"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # toString
    def __str__(self):
        return f"{self.name} is {self.age} years old dog"

    # instance method
    def speak(self):
        print(f"{self.name} says {self.voice}")


pluto = Dog("Pluto", 2)

print(pluto.age)
print(pluto.name)
print(pluto.voice)

# objects are mutable
pluto.age = 3
print(pluto.age)

pluto.speak()

print(pluto)
