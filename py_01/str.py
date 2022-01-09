# mystr = 'да'
# mystr = mystr + 'нет'
# mystr = mystr + 'да'
# print(mystr)

#
# name = input()
# print(f'Футбольная команда {name} имеет длину {len(name)} символов')

# name1 = input()
# name2 = input()
# name3 = input()
#
# print(max(name1, name2, name3, key=len))
# print(min(name1, name2, name3, key=len))

# a = len(input())
# b = len(input())
# c = len(input())
#
# # if ((2*b-c-a)*(2*c-b-a)*(2*a-b-c)) == 0:
# #     print('YES')
# # else:
# #     print('NO')
#
# print('YES' if ((2*b-c-a)*(2*c-b-a)*(2*a-b-c)) == 0 else print('NO'))

# x = input()
# print('YES' if 'синий' in x else print('NO'))

# x = input()
# if 'суббота' in x or 'воскресенье' in x:
#     print('YES')
# else:
#     print('NO')

email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')