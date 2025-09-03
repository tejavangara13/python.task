# Decorator
def example_decorator(func):
    def wrapper():
        print('checking requirement..')
        func()
        print('thank you')     
    return wrapper  
@example_decorator
def printer():
    print('printing the required documents')
printer()