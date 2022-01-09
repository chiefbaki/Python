# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(f'{hours} : {minutes} : {seconds}')

# for i in range(8):
#     for j in range(1 - i):
#         print('*', end='')
#     print()
#
# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print()

# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print(f'x = {x}, y = {y}')
# print(f'Общее количество правильных решений {total}')
#
# counter = 0
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 counter += 1
#                 print(f'n = {n}, k = {k}, m = {m}')
# print(f'Общее количество правильных решений {counter}')
#
# for b in range(101):
#     for k in range(101):
#         for t in range(101):
#             if (10 * b + 5 * k + 0.5 * t == 100) and (b + k + t == 100):
#                 print(b, k, t)
#

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(total + 1, end='')
#         total += 1
#     print()
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print('+')
#
# a, b = int(input()), int(input())
# total_maximum = 0
# s = 0
# for i in range(a, b + 1):
#     maximum = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             maximum += j
#         if maximum > total_maximum:
#             total_maximum = maximum
#             s = j
# print(s, total_maximum)

# n = int(input())
# for i in range(1, n + 1):
#     print(i, end ='')
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print('+', end ='')
#     print()

# n = int(input())
# while n > 9:
#     s = 0
#     while n > 0:
#         last_digit = n % 10
#         s += last_digit
#         n //= 10
#     n = s
# print(n)

# n = int(input())
# while n > 9:
#     n = n // 10 + n % 10
# print(n)
#
# from math import factorial
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += factorial(i)
# print(s)

# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     if [i % j == 0 for j in range(1, i)].count(True) == 1:
#         print(i)

# n = 8
# count = 0
# maximum = -10**6 - 1
# for _ in range(1, n + 1):
#     x = int(input())
#     if x // 4 == 0:
#         count += 1
#     if x < maximum:
#         maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = 4
# count = 0
# maximum = -10 ** 4 - 1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 == 1:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

for i in range(1, )
