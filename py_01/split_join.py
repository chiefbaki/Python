# s = 'Python is on of the best languages'
# words = s.split()
# print(words)

# num = input().split()
# for i in range(len(num)):
#     num[i] = int(num[i])
# print(num)

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# s = input().split()
# for i in range(len(s)):
#     print(s[i])

#s = input().split()
#for i in range(len(s)):
#    print(s[i][0], sep='.', end='.')
    
# s = input().split('\\')
# print('\n'.join(s))    

# s = input().split()
# s1 = ['+'*int(s[i]) for i in range(len(s))]
# print('\n'.join(s1))

# s = input().split('.')
# flag = 'ДА'
# for i in range(len(s)):
#     if int(s[i-1]) <= 255:
#         print(flag)
#         break
#     else:
#         print('НЕТ')
#         break

# s = list(input())
# s1 = input()
# b = s1.join(s)
# print(b) 


# s = {1:10, 2:20, 3:30, 4:40}
# b = [[i, s[i]] for i in s]
# a = [j for i in b for j in i]
# print(a)


n = int(input())
s = []
for i in range(n+1):
    for j in range(i+1):
        if n[i] == n[j]:
            s.append(str(n[i]))
print(s)