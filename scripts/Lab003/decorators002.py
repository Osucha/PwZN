def my_decorator(func):
    print("Hello from my_decorator")
    return func

@my_decorator
def function():
    print("Hello from function")

function()
function()
