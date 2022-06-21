def f(x):
    # x = 42
    return x + 2

lambda x: x + 2

def g(h, x):
    # h = f
    # x = 42
    return h(x) * 2 # Call hàm f, tham số là 42

lambda h,x: h(x) * 2

res = g(f, 42) # Call hàm g, tham số: hàm f, 42
print(res)


def addx(x):
    def _(y):
        return x + y
    return _

add2 = addx(2)
# add2 =
# def _(y):
#     return 2 + y
print(add2(-19))

add3 = addx(3)
# add3 =
# def _(y):
#     return 3 + y
print(add3(-43))


def f(x, y):
    return x * y

def f2(x):
    def _(y):
        return f(x, y)
    return _

a = f2(2) # a = def _(y): return f(2, y)
print(a)
print(a(3))


pi = 3.14159

def change_pi():
    global pi # Nói rằng biến pi là biến ở mức global
    pi = 2.71828

print(pi)
change_pi()
print(pi)


cmd = input('CMD: ')
# flag = None
# if cmd == '1':
#     flag = 'Xin chào'
# else:
#     flag = 'Hello'
# print(flag)

flag = 'Xin chào' if cmd == '1' else 'Hello'
print(flag)


students = [
    {'ID': '000001', 'FullName': 'Cuong Nguyen', 'Birthday': '17/08/1994', 'Sex': '1', 'Address': 'Việt Nam', 'Phone': '0977677010', 'Email': 'cuongnhict@gmail.com'},
    {'ID': '000002', 'FullName': 'Tường An', 'Birthday': '17/08/1994', 'Sex': '0', 'Address': 'Nhật Bản', 'Phone': '0977677010', 'Email': 'tuongan@gmail.com'},
    {'ID': '000003', 'FullName': 'Như Phương', 'Birthday': '17/08/1994', 'Sex': '0', 'Address': 'Nhật Bản', 'Phone': '0977677010', 'Email': 'nhuphuong@gmail.com'},
    {'ID': '000004', 'FullName': 'Phương Thảo', 'Birthday': '02/02/2002', 'Sex': '0', 'Address': 'Việt Nam', 'Phone': '0977777777', 'Email': 'phuongthao@gmail.com'},
    {'ID': '000005', 'FullName': 'Trọng Nghĩa', 'Birthday': '01/01/2000', 'Sex': '1', 'Address': 'Nhật Bản', 'Phone': '1111111111', 'Email': 'nghia@gmail.com'},
    {'ID': '000006', 'FullName': 'Đồng Tài', 'Birthday': '03/03/2003', 'Sex': '1', 'Address': 'Nhật Bản', 'Phone': '1111111111', 'Email': 'tai@gmail.com'}
]

studentsSorted = sorted(students, key=lambda st: st['FullName'].split(' ')[-1])
for st in studentsSorted:
    print(st['FullName'])

def getLastName(st: dict):
    return st['FullName'].split(' ')[-1]
studentsSorted = sorted(students, key=getLastName)
for st in studentsSorted:
    print(st)

def f():
    '''Đây là hàm f
    '''
    print('123')
    ...
    ...
    ...


def my_print(*args): # tuple
    for item in args:
        print(item, end=' ')
    print()

my_print(4, 5, 4, 9, 10, 4, 5, 4, 9, 10, 'a', 'b')


def my_color(**kwargs): # dict
    print(kwargs)

my_color(red=21, green=68, blue=120)

params = {
    'red': 21,
    'green': 68,
    'blue': 120
}
my_color(**params)


def upper_case_decorator(func):
    def wrap(*args, **kwargs):
        text = func(*args, **kwargs)
        return text.upper()
    return wrap

@upper_case_decorator
def hello():
    return 'Hello Everybody!!!'

@upper_case_decorator
def welcome():
    return 'Welcome to Pyhton 03 !!!'

res = welcome()
# Cần phải upper nội dung trả về của hàm hello, mà không được sửa hàm hello
print(res)


class CallCount:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        text = self.func(*args, **kwargs)
        return text.upper()

def add_python_decorator(func):
    def wrap(*args, **kwargs):
        text = func(*args, **kwargs)
        return text + ' Python'
    return wrap

@add_python_decorator   # WELCOME TO PYTHON 03 !!! PYTHON PYTHON PYTHON PYTHON PYTHON Python
@CallCount              # WELCOME TO PYTHON 03 !!! PYTHON PYTHON PYTHON PYTHON PYTHON
@add_python_decorator   # WELCOME TO PYTHON 03 !!! PYTHON PYTHON Python Python Python
@add_python_decorator   # WELCOME TO PYTHON 03 !!! PYTHON PYTHON Python Python
@add_python_decorator   # WELCOME TO PYTHON 03 !!! PYTHON PYTHON Python
@CallCount              # WELCOME TO PYTHON 03 !!! PYTHON PYTHON
@add_python_decorator   # Welcome to Python 03 !!! Python Python
@add_python_decorator   # Welcome to Python 03 !!! Python
def welcome():          # Welcome to Python 03 !!!
    return 'Welcome to Python 03 !!!'

# res = welcome()
# res = welcome()
# res = welcome()
# res = welcome()
# print(res)
# print(welcome.count)

res = welcome()
print(res)


students = [
    {'ID': '000001', 'FullName': 'Cuong Nguyen', 'Birthday': '17/08/1994', 'Sex': 1, 'Address': 'Việt Nam', 'Phone': '0977677010', 'Email': 'cuongnhict@gmail.com'},
    {'ID': '000002', 'FullName': 'Tường An', 'Birthday': '17/08/1994', 'Sex': 0, 'Address': 'Nhật Bản', 'Phone': '0977677010', 'Email': 'tuongan@gmail.com'},
    {'ID': '000003', 'FullName': 'Như Phương', 'Birthday': '17/08/1994', 'Sex': 0, 'Address': 'Nhật Bản', 'Phone': '0977677010', 'Email': 'nhuphuong@gmail.com'},
    {'ID': '000004', 'FullName': 'Phương Thảo', 'Birthday': '02/02/2002', 'Sex': 0, 'Address': 'Việt Nam', 'Phone': '0977777777', 'Email': 'phuongthao@gmail.com'},
    {'ID': '000005', 'FullName': 'Trọng Nghĩa', 'Birthday': '01/01/2000', 'Sex': 1, 'Address': 'Nhật Bản', 'Phone': '1111111111', 'Email': 'nghia@gmail.com'},
    {'ID': '000006', 'FullName': 'Đồng Tài', 'Birthday': '03/03/2003', 'Sex': 1, 'Address': 'Nhật Bản', 'Phone': '1111111111', 'Email': 'tai@gmail.com'}
]
for st in students:
    aliasSex = 'Nam' if st['Sex'] == 1 else 'Nữ' if st['Sex'] == 0 else 'N/A' # Reject elif
    print(st['FullName'], aliasSex)


def aliasSex(st):
    st['Sex'] = 'Nam' if st['Sex'] == 1 else 'Nữ' if st['Sex'] == 0 else 'N/A'
    return st

aliasStudents = list(map(aliasSex, students))
print(aliasStudents)
for st in aliasStudents: # Lúc này map thực hiện
    print(st['FullName'], st['Sex'])


a = ['a1', 'a2', 'a3']
b = ['b1', 'b2', 'b3']
c = ['c1', 'c2', 'c3']
def f(x, y, z):
    print(x, y, z)

list(map(f, a, b, c))


text = 'Xin chào Python 03 !!!'
# Sử dụng hàm map để chuyển text thành upper case
def upper_case(t):
    return t.upper()

text_fix = ''.join(list(map(upper_case, text)))
print(text_fix)


students = [
    {'Code': '000001', 'FullName': 'Cuong Nguyen', 'Birthday': '17/08/1994', 'Sex': 1,
        'Address': 'Việt Nam', 'Phone': '0977677010', 'Email': 'cuongnhict@gmail.com'},
    {'Code': '000002', 'FullName': 'Tường An', 'Birthday': '17/08/1994', 'Sex': 0,
        'Address': 'Nhật Bản', 'Phone': '0977677010', 'Email': 'tuongan@gmail.com'},
    {'Code': '000003', 'FullName': 'Như Phương', 'Birthday': '17/08/1994', 'Sex': 0,
        'Address': 'Nhật Bản', 'Phone': '0977677010', 'Email': 'nhuphuong@gmail.com'},
    {'Code': '000004', 'FullName': 'Phương Thảo', 'Birthday': '02/02/2002', 'Sex': 0,
        'Address': 'Việt Nam', 'Phone': '0977777777', 'Email': 'phuongthao@gmail.com'},
    {'Code': '000005', 'FullName': 'Trọng Nghĩa', 'Birthday': '01/01/2000', 'Sex': 1,
        'Address': 'Nhật Bản', 'Phone': '1111111111', 'Email': 'nghia@gmail.com'},
    {'Code': '000006', 'FullName': 'Đồng Tài', 'Birthday': '03/03/2003', 'Sex': 1,
        'Address': 'Nhật Bản', 'Phone': '1111111111', 'Email': 'tai@gmail.com'}
]
searchContent = input('Nhập nội dung tìm kiếm: ')
studentsFiltered = []
for st in students:
    if st['Code'] == searchContent \
        or searchContent.lower() in st['FullName'].lower() \
            or searchContent.lower() in st['Email'].lower():
        studentsFiltered.append(st)


# Lọc ra các học viên từ students với điều kiện ...
studentsFiltered = list(filter(lambda st: st['Code'] == searchContent or searchContent.lower() in st['FullName'].lower() or searchContent.lower() in st['Email'].lower(),
                               students))
print(studentsFiltered)

for st in studentsFiltered:
    print(st)


lst = [i for i in range(10)]
print(lst)
# []
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

set = {i for i in range(10)}
print(set)

dct = { f'key_{i}': i for i in range(5) }
print(dct)
# {}
# { 'key_0': 0, 'key_1': 1,... }
for key, val in dct.items():
    print(key, val)

lst = ['even' if i % 2 == 0 else 'odd' for i in range(10)]
print(lst)