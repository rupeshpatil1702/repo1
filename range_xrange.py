# Decorator function
def my_decorator(func):
    def wrpper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrpper

# Using the decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()


print(a:=5)