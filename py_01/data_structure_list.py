# arr = ['A', 'B', 'C', 'D', 'E']
# for i in range(len(arr)):
#     print(arr[i], end=' ')
#
# l1 = list(range(1, 10, 2))
# l2 = input()
# l2 = l2.replace(' ', '')
# chars = list(l2)
# print(l1, chars)

# arr = int(input())
# chars = list(range(1, arr+1))
# print(chars)

# l1 = int(input())
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(abc[:l1])

# numbers1 = [1, 2, 3]
# numbers2 = [6] * 6
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1 + numbers2 + numbers3)

# list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
# list1.append('python')
# list1.extend(['python'])
# del list1[-3]
# print(list1)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# del numbers[0]
# del numbers[-1]

# l1 = int(input())
# total = []
# for i in range(1, l1+1):
#     arr = input()
#     total.append(arr)
# print(total)
#

sp = []
for i in range(26):
    sp.append(chr(ord('a') + i) * (i + 1))
print(sp)


