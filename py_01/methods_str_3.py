# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     print(chr(i), end=' ')

# b = input()
# for i in range(len(b)):
#     print(ord(b[i]), end=' ')

# шифр Цезаря

# alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
# encrypt = input('Enter e message: ')
# key = int(input('Enter number: '))
# encrypt = encrypt.lower()
# encrypted = ''
#
# for letter in encrypt:
#     position = alphabet.find(letter)
#     new_position = position - key
#     if letter in alphabet:
#         encrypted += alphabet[new_position]
#     else:
#         encrypted += letter
# print(encrypted)

# a = input()
# if a.endswith('00'):
#     print('YES')
# else:
#     print('NO')
#
# x1, x2, y1, y2 = int(input()), int(input()), int(input()), int(input())
# sum = x1 + x2 + y1 + y2
# if sum % 2 == 0:
#     print("YES")
# else:
#     print("NO")
#
# age = int(input())
# sex = input()
# if 10 <= age <= 15 and 'f' in sex:
#     print('YES')
# else:
#     print('NO')

s = input()
if s.find('f') == 1:
    print(-1)
elif s.find('f') == 0:
    print(-2)
else:
    s.replace('f','',1)
    print(s.find('f'))