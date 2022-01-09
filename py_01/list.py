# list = [
#     ['apple','watermelon','strawberry','orange'],
#     ['cucumber','potato','tomato']
# ]
# for i in enumerate(list):
#     for j in enumerate(list):
#         print(j)
#     print()
# lst = [lst + d for lst in 'tea' if lst != 't' for d in 'spam' if d != 'm']
# print(lst)


# l = ['a','b','c']
# list = [1,2,3,4,5,6]
# list.append([7,8,9])
# list.extend(l)
# list.pop(3)

# str_ = 'John' + 'Alex' + 'Tate' + 'Suarez'
# names = ['John','Alex','Tate','Suarez']
# print(str_[:6])
# print(names.index('Alex'))
# sort = sorted(names)
#
# numbers = [1,2,3,4,5,6,7,8,9]
# b = numbers
# b[1] = 'B'
# a = b
# a[2] = 'C'
# print(a)
#
# lst = [int(i) for i in input().split()]
# summ = sum(lst)
# print(summ)

# l = [True,243,3,43,43,4]
# l.remove(True)
# print(l)

# from math import pow

# x = int(input())
# l1 = []
# for i in range(x):
#     l = int(input())
#     cnt = l ** 3 
#     l1.append(cnt)
# print(l1)

# x = int(input())
# l = []
# cnt = 1
# for i in range(1, x + 1):
#     if x % i == 0:
#         l.append(i)
# print(l)


# x = int(input())
# l = []
# l2 = []
# for i in range(x):
#     n = int(input())
#     l.append(n)
# for i in range(len(l) - 1):
#     l2.append(l[i] + l[i + 1])
# print(l2)

# x = int(input())
# l = []
# for i in range(x):
#     n = int(input())
#     l.append(n)
# del l[1::2]
# print(l)



l1 = [1, 2, 3, 4, 5]
del l1[4]
print(l1)