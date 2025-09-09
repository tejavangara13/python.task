#Polymorphism types
class Calculator:
    
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add())          
print(calc.add(5))         
print(calc.add(5, 10))     
print(calc.add(5, 10, 20)) 

#runtime overloading

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())  

 # operator overloading
class Book:
    def __init__(self, pages):
        self.pages = pages

   
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book(100)
book2 = Book(200)
print(book1 + book2)  


class Pycharm:
    def execute(self):
        print("Compiling and Running in PyCharm")

class VSCode:
    def execute(self):
        print("Compiling and Running in VS Code")

def run_ide(ide):
    ide.execute()

run_ide(Pycharm())  
run_ide(VSCode())   
