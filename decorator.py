def decorator(func):
    def wrapper(*args):
        print("in Decorator")
        result = func(*args)
        return result
    return wrapper

@decorator
def display(*name):
    print(f"Hi My name is {name}")

display("Dishant" , "Bhavya")
