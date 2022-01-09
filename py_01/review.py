# review of code 1
# count = 0
# p = 1
# for _ in range(1, 10 + 1):
#     x = int(input())
#     if x >= 0:
#         p *= x
#         count += 1
# if count != 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# review of code 2
# mx = -10**6 - 1
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x < 0 and x > mx:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# review of code 3
# s = 0
# for i in range(1, 7 + 1):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# if s % 2 == 1:
#     print(0)
# else:
#     print(s)

# review of code 4
# n = int(input())
# while n > 9:
#     largest = n % 10
#     n //= 10
# print(n)

# review of code 5
n = int(input())
product = 1
while n >= 1:
    digit = n % 10
    product *= digit
    n //= 10
print(product)