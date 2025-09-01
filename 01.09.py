#oops concepts

# Class definition
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Arithmetic operations
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b if self.b != 0 else "Division by zero error"
    
    def mod(self):
        return self.a % self.b
    
    def power(self):
        return self.a ** self.b


# Create objects
obj1 = Calculator(10, 5)
obj2 = Calculator(20, 4)

# Add extra attributes to obj1
obj1.model_num = "ABC123"
obj1.made_in = "India"

# Add extra attributes to obj2
obj2.color = "Red"
obj2.discount = "10%"

# Print attributes
print("Object 1:")
print("Model Number:", obj1.model_num)
print("Made In:", obj1.made_in)

print("\nObject 2:")
print("Color:", obj2.color)
print("Discount:", obj2.discount)

# Calling arithmetic methods
print("\nArithmetic Operations with obj1:")
print("Addition:", obj1.add())
print("Subtraction:", obj1.sub())
print("Multiplication:", obj1.mul())
print("Division:", obj1.div())
print("Modulo:", obj1.mod())
print("Power:", obj1.power())

#define a self
class Sample:
    def __init__(self, name):
        self.name = name   
    
    def show(self):
        print("Name is:", self.name)

obj = Sample("Tejaswi")
obj.show()   


