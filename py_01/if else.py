# p = input()
# a = input()
# if p == a:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')
#
# n = int(input())
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# n = input()
# if (int(n[0]) + int(n[-1])) == (int(n[1]) - int(n[2])):
#     print('ДА')
# else:
#     print('НЕТ')

# n = int(input())
# if n >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# a = int(input())
# b = int(input())
# c = int(input())
# if b - a == c - b:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# if a > b:
#     print(b)
# else:
#     print(a)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min(a,b,c,d))

# a = int(input())
# if a <= 13:
#     print('детство')
# elif a < 24:
#     print('молодость')
# elif a <= 59:
#     print('зрелость')
# elif a >= 60:
#     print('старость')

a = int(input())
b = int(input())
c = int(input())
s = 0
if a > 0:
    s += a
if b > 0:
    s += b
if c > 0:
    s += c
print(s)
