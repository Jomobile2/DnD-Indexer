# from pathlib import Path

# p = Path(".")
# print(p)
# print(p.exists())
# print()

# p2 = p / "randomstuff.txt"
# print(p2)
# print(p2.exists())
# print()

# p3 = p / "asldfkjsdlfk.txt"
# print(p3)
# print(p3.exists())
# print()
# p3.write_text("Another way")
# p = Path('.')
# [x for x in  p.iterdir() if x.is_dir()]


#Classes vs Instances: Object Oriented Programming:

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         pass

#     Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.
# On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().
# For example, the following Dog class has a class attribute called species with the value "Canis familiaris":

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# jestus = Dog("Jestus", 4)
# martinez = Dog("Martinez", 9)

# print(f"{jestus.age}")

# jestus.age = 100
# print(f"{jestus.age}")

# dog.py
#WHEN DOUBLE PARENTHESIS, INVERT QUOTATIONS, ONE "", OTHER ''
# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# jestus = Dog("Jestus", 10)
# jestus.description()
# print(f"{jestus.description()}")
# jestus.speak("Woof Woof")
# print(f'{jestus.speak("rwsfsf")}')
# jestus.speak("Bow Wow")
# print (f"{jestus.speak()}")
# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def __repr__(self):
#         return f"Dog(name='{self.name}', age={self.age})"
    
#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# jestus = Dog("Jestus", 10)
# print(jestus.speak("rah"))

from dataclasses import dataclass

@dataclass
class Snake:
    name: str
    age: int
    apple: int

    def name_and_age(self):
        return f"{self.name} is {self.age} years old"
    
    def name_and_apple(self):
        return f"{self.name} has {self.apple} apples"
    

# Signame = input("What is their name?")
# SigAge = int(input("What is their age?"))
# SigApple = int(input("How many apples"))
Sig = Snake("Rah", 5, 50)
# print(f"{Sig.name_and_age()}")
# print(f"{Sig.name_and_apple()}")
# print(f"{Sig}")
    
print(f"{Sig.name_and_apple()}")