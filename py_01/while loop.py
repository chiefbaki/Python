# i = 1
# while i <= 10:
#     print(f'Hello, World! {i}')
#     i += 1

#
#
# num = int(input())
# while num != -1:
#     print('Hello,World!')
#     num = int(input())
#
# text = input()
# total = 0
# while text != 'stop':
#     n = int(text)
#     total += n
#     text = input()
# print(total)

# n = int(input())
# while n != -1:
#     print(f'Квадрат числа равен {n * n}')
#     n = int(input())



# text = input()
# while text != 'КОНЕЦ' or text != 'конец':
#     print(text)
#     text = input()

# text = input()
# total = 0
# while text != 'стоп' and 'хватит' and 'достаточно':
#     text = input()
#     total += 1
# print(total)

# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())

# num = int(input())
# total = 0
# while num >= 0:
#     total += num
#     num = int(input())
# print(total)

# num = int(input())
# total = 0
# while 0 < num < 6:
#     if num == 5:
#         total += 1
#     num = int(input())
# print(total)

# num = int(input())
# total = 0
# while num >= 25:
#     total += 1
#     num -= 25
# while num >= 10:
#     total += 1
#     num -= 10
# while num >= 5:
#     total += 1
#     num -= 5
# while num >= 1:
#     total += 1
#     num -= 1
# print(total)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# n = int(input())
# while n != 0:
#     last_digit = n % 10
#     print(last_digit)
#     n //= 10

# n = int(input())
# while n != 0:
#     last_digit = n % 10
#     n //= 10
#     print(last_digit, end='')

# n = int(input())
# find_seven = True
#
# while n != 0:
#     last_digit = n % 10
#     if last_digit == 7:
#         find_seven = True
#     else:
#         find_seven = False
#     n //= 10
# if find_seven == True:
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# counter = 0
# multi = 1
# total = 0
# last_digit = n % 10
# sum = 0
# first_digit = 0
# while n != 0:
#     total += n % 10
#     counter += 1
#     multi *= n % 10
#     ar = total / counter
#     if n // 10 == 0:
#         first_digit = n
#     sum = first_digit + last_digit
#     n //= 10
# print(total)
# print(counter)
# print(multi)
# print(ar)
# print(first_digit)
# print(sum)

# n = int(input())
# b = n % 10
# flag = 'YES'
# while n > 0:
#     if b != n % 10:
#         flag = 'NO'
#     n //= 10
# print(flag)

n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(i)