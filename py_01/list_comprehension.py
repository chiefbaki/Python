# a = [int(input()) for i in range(int(input()))]
# print(a)

# a = [i + j for i in range(5) for j in range(3)]
# print(a)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# lengths = [len(i) for i in keywords]

# print(lengths)

# n = int(input())
# copy_n = n 
# result = 0
# while n != 0:
#     digit = n % 10 
#     result = result * 10 + digit
#     n //= 10
# print(f'Result is: {result}')
# if result == copy_n:
#     print('Its palindrom')
# else:
#     print('Not palindrom')

# palindromes = [i for i in range(100,1001) if str(i) == str(i)[::-1]]

# print(palindromes)

# a = [i**2 for i in range(1, int(input())+1)]
# for i in a:
#     print(i)


# print(*[int(i) ** 3 for i in input().split()], sep='\n')


# print(*[i for i in input() if i in '1234567890'],sep='')

# print(*[int(i) ** 2 for i in input().split() if (int(i)**2 % 2 == 0) and (int(i)**2 % 10 != 4)])

# l1 = [int(i) for i in input().split()]
# l2 = [int(i) for i in input().split()]
# print(*[a + b for a, b in zip(l1, l2)])

# num = [int(i) for i in input().split()]
# print(*num, sep='+', end='=' f'{sum(num)}')

# a = [len(i) for i in input().split()]
# print(max(a))

# print(*[str(i)[1:] + str(i)[0] + 'ки' for i in input().split()])

