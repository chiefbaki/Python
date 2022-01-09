# поиск и замена

# s = input()
# print(s.count('o'))
# print(s.count('o', 5))
# print(s.startswith('hello'))
# print(s.endswith('g'))
# print(s.find('foo'))
# print(s.strip()) возвращает копию строки s у которой удалены все пробелы стоящие в начале и конце строки.
# print(s.replace('foo', 'hello', 3)) заменяет old на new и имеет необз-й аргумент count !

# print(input().count() + 1)
#
# t = input()
# t = t.lower()
# print(f'Аденин : {t.count("а")}')
# print(f'Гуанин : {t.count("г")}')
# print(f'Цитозин : {t.count("ц")}')
# print(f'Тимин : {t.count("т")}')

# n = int(input())
# cnt = 0
# for i in range(n):
#     t = input()
#     if int(t.count('11')) >= 3:
#         cnt += 1
# print(cnt)

# n = input()
# cnt = 0
# for i in range(len(n)):
#     if int('0'<=n[i]<='9'):
#         cnt += 1
# print(cnt)

# n = input()
# flag = 'NO'
# for i in range(len(n)):
#     if n.endswith('.com' or '.ru'):
#         flag = 'YES'
# print(flag)

n = input()
max = 0
b = 0
for i in range(len(n)):
    if n.count([i]) >= max:
        max = n.count([i])
        b = [i]
        print(b)

