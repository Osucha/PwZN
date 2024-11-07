def my_generator():
    yield 'xD'
    yield 'YOLO'
    yield 'LOL'

# print(type(my_generator))
# print(type(my_generator()))

# for s in my_generator():
#     print(s)

def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in my_range(5):
    print(i)

rng = list(my_range(5))
print(rng)