# pass

# def function():
#     pass

# class Student:
#     pass

# s1 = Student()
# print(type(s1))

# class Student:
#     classes = []

#     def __init__(self):
#         print('init student')

# s1 = Student()
# s1.classes.append('Math')
# s1.classes.append('Physics')
# s1.classes.append('Chemistry')
# print(s1.classes)

# s2 = Student()
# print(s2.classes)

# print(Student.__dict__)
# print(s1.__dict__)

# class Student:
#     def __init__(self):
#         self.classes = []
#         print('init student')

# s1 = Student()
# s1.classes.append('Math')
# s1.classes.append('Physics')
# s1.classes.append('Chemistry')
# print(s1.classes)

# s2 = Student()
# print(s2.classes)

# s1.age = 20

# print(Student.__dict__)
# print(s1.__dict__)

# class Student:
#     def __init__(self):
#         self.classes = []
#         print('init student')
    
#     def print_classes(self):
#         print(self.classes)

# s1 = Student()
# s1.classes.append('Math')
# s1.classes.append('Physics')
# s1.classes.append('Chemistry')

# s1.print_classes()
# Student.print_classes(s1)
# Student.__dict__['print_classes'](s1)


# print(Student.__dict__)
# print(s1.__dict__)

class Student:
    def __init__(self):
        self.classes = []
        print('init student')
    
    def print_classes(self):
        print(self.classes)

    def __getitem__(self, index):
        print(index)
        return 'YOLO'
    
s1 = Student()
x = s1['xzzxxczxcz']
print(x)