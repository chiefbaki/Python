# letter = ["a", "b", "c", "d"]
#
# print(*letter)
#
# list = [10, 20, 30, 40, 60]
#
# print(*list)
#
# s = 'PYTHON'
# print(*s, sep='*, \n')


# сумма квадратор перебираемых элементов
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# total = 0
# for i in range(len(numbers)):
#     a = numbers[i] * numbers[i]
#     total += a
# print(total)


# n = int(input())
# arr = []
# for i in range(n):
#     x = int(input())
#     arr.append(x)
# for j in range(n):
#     arr.remove(min(arr))
#     arr.remove(max(arr))
# print(*arr, sep='\n')
#
#


n = int(input())
list = []
for i in range(n):
    unique_list = []
    s = input()
    list.append(s)
    unique = set(list)
    unique_list.append(list(unique))
print(*unique_list, sep='\n')