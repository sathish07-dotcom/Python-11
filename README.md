
📘 Polymorphism in Python
🔍 What is Polymorphism?
Polymorphism is an important concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as if they are of the same class. In Python, polymorphism allows different objects to respond to the same method or operation in different ways.

✅ “Many forms, one interface.”

🔸 Types of Polymorphism in Python
1. Duck Typing (Dynamic Typing)
In duck typing, the type or class of an object is less important than the methods it defines.

python
Copy
Edit
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def lift_off(entity):
    entity.fly()

lift_off(Bird())       # Bird can fly
lift_off(Airplane())   # Airplane can fly
2. Operator Overloading
Python allows customizing the behavior of operators for user-defined classes by defining special methods like __add__, __sub__, etc.

python
Copy
Edit
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)
print(a + b)  # 30
3. Method Overriding (Runtime Polymorphism)
Subclass provides a specific implementation of a method already defined in its parent class.

python
Copy
Edit
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
d = Dog()

a.sound()  # Some sound
d.sound()  # Bark
4. Method Overloading (Simulated using default arguments)
Python doesn't support traditional method overloading, but similar behavior can be achieved using default arguments.

python
Copy
Edit
class Greet:
    def hello(self, name=None):
        if name:
            print(f"Hello, {name}")
        else:
            print("Hello")

g = Greet()
g.hello()         # Hello
g.hello("Sathish")  # Hello, Sathish
✅ Why Use Polymorphism?
Increases flexibility and scalability of code

Improves code readability and reusability

Makes code more maintainable

📌 Real-World Use Cases
Shape classes like Circle, Square, and Triangle all have a draw() method.

In AI recruitment platforms, different job/candidate matchers can have a common match() method.

In fitness tracker apps, different workout types (Cardio, Yoga, Strength) can have a shared start() method.

📂 Polymorphism simplifies programming by allowing the same interface to work with different underlying forms (data types or classes).
