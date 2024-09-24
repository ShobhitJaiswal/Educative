def my_decorator(func):
    def wrapper(a):
        print("Something is happening before the function is called.")
        func(a)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(a):
    print("Hello!",a)

say_hello(10)
