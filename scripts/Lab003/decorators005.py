from functools import wraps

def my_decorator(func = None, a = 'lol', b = 'rotfl'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.", a, b)
            func(*args, **kwargs)
            print("Something is happening after the function is called.", a, b)
        return wrapper
    
    if func is None:
        return decorator
    else:
        return decorator(func)

    return decorator

@my_decorator(a = 'xD', b = 'yolo')
def function(x, y, z):
    print("Hello from function: ", x, y, z)

# function = my_decorator(1, 2)(function)

#function(1, 2, 3)
print(function.__name__)