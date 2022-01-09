from math import *
# n = int(input())
# total = 0
# for i in range(1,n + 1):
#     if i % 10 == 5:
#         total += i
# print(total)

# n = int(input())
# for i in range(1, n + 1):
#     x = factorial(i)
# print(x)

# total = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)

# n = int(input())
# total = 0
# for i in range(1, n  + 1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)

#
# n = int(input())
# prelargest = 0
# largest = 0
# for _ in range(1, n + 1):
#     n = int(input())
#     if n > largest:
#         prelargest = largest
#         largest = n
#     elif prelargest < n < largest:
#         prelargest = n
# print(largest)
# print(prelargest)
#
# total = 0
# for _ in range(10):
#     n = int(input())
#     if n % 2 == 0:
#         total += 1
# if total == 10:
#     print('YES')
# else:
#     print('NO')

total = 0
s = 1
n = int(input())
for i in range(1, n + 1):
    b = s
    s = b + total
    total = b
    print(b, end=' ')