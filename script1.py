# print(3 + 1)
# print(3 * 3)
# print (2 ** 3)
# print("Hello, world!")

# print('py' + 'thon')
# print('py' * 3 + 'thon')
#print('py' - 'py')
#print('3' + 3)
#print(3 * '3')
#print(a)
# a = 3
# print(a)

# print(1 == 1)
# print(1 == True)
# print(0 == True)
# print(0 == False)
# print(3 == 1 * 3)
# print((3 == 1) * 3)
# print((3 == 3) * 4 + 3 == 1)
# print(3**5 >= 4**4)

# print(5 / 3)
# print(5 % 3)
# print(5.0 / 3)
# print(5 / 3.0)
# print(5.2 % 3)
# print(2001 ** 200)

#print(2000.3 ** 200)
# print(1.0 + 1.0 - 1.0)
# print(1.0 + 1.0e20 - 1.0e20)

# name='pavani'
# print(f"Hello, {name}!")

# print(float(123))
# print(float('123'))
# print(float('123.23'))
# print(int(123.23))
#print(int('123.23'))
#print(int(float('123.23')))
# print(str(12))
# print(str(12.2))
# print(bool('a'))
# print(bool(0))
# print(bool(0.1))

# print(range(5))
# for i in range(5):
#     print(i)
# print(type(range(5)))

# for i in range(101):
#     print(i)

# for i in range(101):
#     if i%7==0:
#         print(i)

# for i in range(1,100):
#     if (i%5 == 0 and i%3 !=0):
#         print(i)

# for x in range(2,21):
#     for i in range(2,21):
#         if x % i == 0:
#             if x != i:
#                 print(i)

# n = 0
# x = 1
# while n<20:
#     if x%5 == x%7== x%11 == 0:
#         print(x)
#         n = n+1
#     x = x+1

# def hello_world():
#     print('Hello, world!')
# hello_world()

# def hello_name(name):
#     print(f'Hello, {name}!')
# hello_name('Pavani')

# def poly(x):
#     print(3*(x ** 2) - x + 2)
# poly(3)

# def my_max(x,y):
#     if x>y:
#         print(f'{x} is greater than {y}')
#     else:
#         print(f'{y} is greater than {x}')
# my_max(12,16)
# my_max(44,12)

# def my_max(x,y):
#     max_value = x
#     if y>x:
#         max_value = y
#     return max_value
# print(my_max(12,18))
# print(my_max(37,28))
########################################################
# x=5
#
# if x==2:
#     print("prime")
# else:
#     if x % 2 != 0:
#         for i in range(1,x):
#             if (i % 1 == 0 and i % x == 0):
#                 print(1, i)
#     else:
#         print("Not a prime")
########################################################
# def is_prime(num):
#     if num > 1:
#         for i in range(2, (num // 2) + 1):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# print(is_prime(97))

# def list_func(new_list):
#     for i in new_list:
#         print(i)
#
# new_list = [2, 3, 5, 7, 11, 13]
# list_func(new_list)

# def reverse_list_func(new_list):
#    rev_list = new_list[::-1]
#    print(rev_list)
#
# new_list = [10, 11, 12, 13, 14, 15]
# reverse_list_func(new_list)

# def len_func(new_list):
#      x = len(new_list)
#      print(x)
#
# new_list = [2, 7, 11, 13]
# len_func(new_list)