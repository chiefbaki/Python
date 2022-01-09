# конвертация регистра

t = 'Hello'
print(t.find('e'))

a = input()
# print(a.capitalize()) писать прописными буквами, закрепить.
# print(a.swapcase()) обменять регистр. swap
# print(a.title()) заголовок, титул.
# print(a.lower()) нижний
# print(a.upper()) верхний

# Одно очень важное замечание о методах данной категории состоит в том, что они не изменяют исходную строку.
# Если вы хотите изменить строку s нужно написать код: s = s.lower().
a = a.swapcase()
print(a)

# x = input()
# if x.istitle():
#     print('YES')
# else:
#     print('NO')

# x = input()
# x = x.lower()
# if 'хорош' in x:
#     print('YES')
# else:
#     print('NO')

# x = input()
# cnt = 0
# for i in range(len(x)):
#     if x.islower():
#         cnt += 1
# print(cnt)

