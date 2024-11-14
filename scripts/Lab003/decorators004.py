def my_decorator(a = 'lol', b = 'rotfl'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.", a, b)
            func(*args, **kwargs)
            print("Something is happening after the function is called.", a, b)
        return wrapper
    
    return decorator

@my_decorator('xD', 'yolo')
def function(x, y, z):
    print("Hello from function: ", x, y, z)

# function = my_decorator(1, 2)(function)

function(1, 2, 3)