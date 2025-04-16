

## **1. Method Overriding (Basic Example)**

class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

a = Animal()
d = Dog()
print(a.make_sound())  # Output: Some sound
print(d.make_sound())  # Output: Bark



## **2. Overriding Parent Method using `super()`**

class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return super().greet() + " and Hello from Child"

c = Child()
print(c.greet())  



## **3. Polymorphism with Function**

class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Bark"

def make_animal_speak(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()

make_animal_speak(cat)  
make_animal_speak(dog)  



## **4. Operator Overloading (`+` for Custom Objects)**

class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Point(self.x + other.x)

p1 = Point(10)
p2 = Point(20)
result = p1 + p2
print(result.x)  # Output: 30



## **5. Operator Overloading (`*` Overloading)**

class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Number(self.value * other.value)

n1 = Number(3)
n2 = Number(4)
result = n1 * n2
print(result.value)  # Output: 12



## **6. Polymorphism with Built-in Functions**

print(len("Hello"))  # Output: 5
print(len([1, 2, 3, 4]))  # Output: 4
print(len({"name": "Sathish", "age": 25}))  # Output: 2



## **7. Function Overloading using Default Arguments**

class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(2))        # Output: 2
print(m.add(2, 3))     # Output: 5
print(m.add(2, 3, 4))  # Output: 9



## **8. Duck Typing Example**

class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

def start_flying(obj):
    print(obj.fly())

b = Bird()
a = Airplane()
start_flying(b)  
start_flying(a)  



## **9. Method Overloading using Variable Arguments (`*args`)**

class MathOperations:
    def add(self, *args):
        return sum(args)

m = MathOperations()
print(m.add(2, 3))       # Output: 5
print(m.add(2, 3, 4))    # Output: 9
print(m.add(2, 3, 4, 5)) # Output: 14



## **10. Polymorphism in Inheritance**

class Vehicle:
    def type(self):
        return "Generic Vehicle"

class Car(Vehicle):
    def type(self):
        return "Car"

class Bike(Vehicle):
    def type(self):
        return "Bike"

v = Vehicle()
c = Car()
b = Bike()

print(v.type())  # Output: Generic Vehicle
print(c.type())  # Output: Car
print(b.type())  # Output: Bike



## **11. Abstract Class and Method Overriding**

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

d = Dog()
print(d.sound())  



## **12. Polymorphism in Different Classes**

class Rectangle:
    def area(self, length, breadth):
        return length * breadth

class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

shapes = [Rectangle(), Circle()]
print(shapes[0].area(5, 10))  
print(shapes[1].area(7))  



## **13. Using `isinstance()` in Polymorphism**

class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))     # Output: True
print(isinstance(d, Animal))  # Output: True



## **14. Checking Subclass with `issubclass()`**

class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))  # Output: True



## **15. Method Resolution Order (MRO) in Multiple Inheritance**

class A:
    def show(self):
        return "Class A"

class B(A):
    def show(self):
        return "Class B"

class C(A):
    def show(self):
        return "Class C"

class D(B, C):
    pass

d = D()
print(d.show())  # Output: Class B (Based on MRO)



## **16. Method Resolution Order (MRO) using `super()`**

class A:
    def show(self):
        return "Class A"

class B(A):
    def show(self):
        return super().show() + " -> Class B"

class C(B):
    def show(self):
        return super().show() + " -> Class C"

c = C()
print(c.show())  



## **17. Overloading `>` Operator**

class Number:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

n1 = Number(10)
n2 = Number(5)
print(n1 > n2)  # Output: True



## **18. Overloading `__str__` Method**

class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Car Model: {self.model}"

c = Car("Tesla")
print(c)  



## **19. Overloading `__len__` Method**

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

b = Book(300)
print(len(b))  # Output: 300



## **20. Function Overloading with `@staticmethod`**

class Math:
    @staticmethod
    def multiply(a, b, c=1):
        return a * b * c

print(Math.multiply(2, 3))     # Output: 6
print(Math.multiply(2, 3, 4))  # Output: 24


