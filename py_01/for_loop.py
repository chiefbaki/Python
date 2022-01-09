# for i in range(10+1):
#     print('Python is awesome!')

# str1 = input()
# x = int(input())
# for i in range(x):
#     print(str1)

# for i in range(6):
#     print('AAA')
# for j in range(5):
#     print('BBBB')
# print('E')
# for x in range(9):
#     print('TTTTT')
# print('G')

# n = int(input())
# for i in range(n):
#     print('*' * 19)

# n = int(input())
# x = input()
# for i in range(n):
#     print(i, x)

# n = int(input())
# for i in range(n+1):
#     print(f'Квадрат числа равен {i} {i*i}')

# n = int(input())
# for i in range(n):
#     print('*' * n)
#     n -= 1

# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(m):
#     print(i, float(m))
#     m += m * p / 100

# m = int(input())
# n = int(input())
# for i in range(m, n+1):
#     print(i)

# m = int(input())
# n = int(input())
# if m <= n:
#     for i in range(m, n+1):
#         print(i)
# elif m >= n:
#     for i in range(m, n-1, -1):
#         print(i)
# else:
#     print(n)

# m = int(input())
# n = int(input())
# for i in range(m,n-1,-1):
#     if i % 2 == 1:
#         print(i)

# m = int(input())
# n = int(input())
# for i in range(m, n+1):
#     if i % 17 == 0:
#         print(i)
#     elif i % 10 == 9:
#         print(i)
#     elif i % 3 == 0 and i % 5 == 0:
#         print(i)

# n = int(input())
# for i in range(1, 10):
#     print(f'{n} x {i} = {n * i}')

# s = 0
# for i in range(1,4):
#     n = int(input())
#     if n > 2:
#         s += i
# print(f'Было введено {s}')

# max and min
# largest = -1
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print(largest)

# total = 0
# for i in range(1,6):
#     total += i
#     print(total, end='')


# a = int(input())
# b = int(input())
# total = 0
# for i in range(a, b+1):
#     cube = i ** 3
#     if cube % 10 == 4 or cube % 10 == 9:
#         total += 1
# print(total)

# n = int(input())
# total = 0
# for i in range(n):
#     m = int(input())
#     total += m
# print(total)

# from math import log
# n = int(input())
# total = 0
# for i in range(1,n+1):
#     total += 1/i
# print(total - log(n))

