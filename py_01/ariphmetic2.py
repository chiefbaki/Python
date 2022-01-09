# b = int(input())
# q = int(input())
# n = int(input())
# geo = b * q ** (n - 1)
# print(geo)
#
# t = int(input())
# print(int(t/100))
#

# pupil = int(input())
# m = int(input())
# s = m % pupil
# q = m // pupil
# print(s)
# print(q)
#
# n = int(input())
# even = n - n // 2
# print(even)

# n = int(input())
# t = (n + 3) // 4
# print(t)

# m = int(input())
# h = m // 60
# s = m % 60
# print(f'{m} мин - это {h} час {s} мин.')

# n = int(input())
# a = n % 10
# b = (n % 100) // 10
# c = n // 100
# sum = a + b + c
# deg = a * b * c
# print(f'Сумма цифр = {sum}')
# print(f'Произеведение цифр = {deg}')

n = input()

print(f'Цифра в позиции тысяч равна {n[0]}')
print(f'Цифра в позиции сотен равна {n[1]}')
print(f'Цифра в позиции десятков равна {n[2]}')
print(f'Цифра в позиции единиц равна {n[3]}')