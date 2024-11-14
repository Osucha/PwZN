# def function(x, y, *args, z = 18, **kwargs):
#     print(x, y)
#     print(args)
#     print(z)
#     print(kwargs)

# function(1, 2, 5, 8, 'xD', yolo = 89)

t = (1, 2, 3, 4, 5)
# a = t[0]
# b = t[1]
# c = t[2]
# d = t[3]
# e = t[4]
# print(a, b, c, d, e)

# a, b, c, d, e = t
# print(a, b, c, d, e)

# a, b, *c = t
# print(a, b, c)

# a, b, *_ = t
# print(a, b)

def function(*args, **kwargs):
    print(args)
    print(kwargs)

a = (1, 2, 3, 4, 5)
d = {'x': 1, 'y': 2, 'z': 3}
# function(a[0], a[1], a[2], a[3], a[4])

function(*a, **d)


 