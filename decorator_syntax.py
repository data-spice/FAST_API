import time

def greet_decorator(func):
    def wrapper():
        print("Start of the decorator")
        time.sleep(1)
        func()
        print("End of decorator")
    return wrapper
    
@greet_decorator
def count():
    for x in range(1,4):
        print(x)
        time.sleep(1)



count()