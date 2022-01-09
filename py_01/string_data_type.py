# text = input()
# for i in range(len(text)):
#     if i % 2 == 0:
#         print(text[i])

# t = input()
# for i in reversed(range(len(t))):
#     print(t[i])

# s = input()
# n = input()
# o = input()
# print(s[0], n[0], o[0], sep='')

# n = input()
# total = 0
# for i in n:
#     total += int(i)
# print(total)

# t = input()
# flag = 'Цифр нет'
# for i in range(len(t)):
#     if t[i] in '0123456789':
#         print('Цифра есть')
#         break
# print(flag)

# t = input()
# cnt1 = 0
# cnt2 = 0
# for i in range(len(t)):
#     if t[i] in '+':
#         cnt1 += 1
#     if t[i] in '*':
#         cnt2 += 1
# print(f'Символ + встречается {cnt1} раз')
# print(f'Символ * встречается {cnt2} раз')

# t = input()
# cnt = 0
# for i in range(len(t)-1):
#     if t[i] == t[i + 1]:
#         cnt += 1
# print(cnt)

# t = input()
# cnt1 = 0
# cnt2 = 0
# for i in range(len(t)):
#     if t[i] in 'ауоыиэяюёе':
#         cnt1 += 1
#     if t[i] in 'бвгджзйклмнпрстфхцчшщ':
#         cnt2 += 1
# print(f'Количество гласных букв равно {cnt1}')
# print(f'Количество согласных букв равно {cnt2}')

# n = int(input())
# b = ''
# while n != 0:
#     b += str((n % 2))
#     n //= 2
# print(b[::-1])

# n = input()
# flag = 'NO'
# for i in range(1, len(n)):
#     if n[:] == n[::-1]:
#         flag = 'YES'
# print(flag)
#
# t = input()
# total = 0
# for i in range(len(t)):
#     total += 1
#     cnt = t * 3
# print(total)
# print(cnt)
# print(t[0])
# print(t[:3])
# print(t[-3:])
# print(t[::-1])
# print(t[1:-2])

# t = input()
# print(t[2])
# print(t[-2])
# print(t[:5])
# print(t[:-2])
# print(t[::2])
# print(t[1::2])
# print(t[::-1])
# print(t[::-2])

t = input()
s = [:(len(t))-(len(t)//2)]
print(s)

