# class FunctionObject:
#     def __call__(self, x):
#         print("FunctionObject.__call__", x)

# o = FunctionObject()
# o(5)

class ObjectDecorator:
    def __init__(self, func):
        print("Hello from ObjectDecorator")
        self.func = func
        self.counter = 0
    
    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.", self.counter)
        self.func(*args, **kwargs)
        print("Something is happening after the function is called.")
        self.counter += 1

@ObjectDecorator
def function():
    print("Hello from function")

#function = ObjectDecorator(function)

function()
function()
function()
function()
function()
function()

