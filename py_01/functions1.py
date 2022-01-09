# # def draw_box():
# #     for i in range(14):
# #           print('*' + '* '[0 < i < 13] * 8 + '*')

# # draw_box()

# def draw_triangle():
#     for i in range(1, 11):
#         for j in range(1, i+1):
#             print('*', end='')
#         print()
# draw_triangle()

# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)


# print_number(2, 3, 11)

# объявление функции
def draw_triangle(fill, base):
    
    for i in range(base):
        k = (base // 2 + 1) - abs(base // 2 - i)
        for _ in range(k):
            print(fill, end='')
        print()
# считываем данные
# fill = input()
# base = int(input())

# вызываем функцию

some_num = 20 

def sum_num():
    num = some_num + x
    y = 5 



# объявление функции
def get_factors(num):
    return [i for i in range(1, num+1) if num % i == 0]
    

# считываем данные
# n = int(input())

# вызываем функцию


# объявление функции
def number_of_factors(num):
    a = [i for i in range(1, num+1) if num % i == 0]
    cnt = 0 
    for i in a:
        cnt += 1
    return cnt

# считываем данные
# n = int(input())

# вызываем функцию


# объявление функции
def merge(list1, list2):
    l1 = len(list1)
    l2 = len(list2)
    empty_list = []

    i = 0
    j = 0

    while i < l1 and j < l2:
        if l1[i] < l2[j]:
            empty_list.append(list1[i])
            i += 1
        else:
            empty_list.append(list2[j])
            j += 1

    empty_list += list1[i:] + list2[j:]

    return empty_list

# считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# вызываем функцию

def merge_lists(l1, l2):
    merge = l1 + l2 
    merge.sort()
    return merge

list1 = [int(i) for i in input().split()]
list2 = [int(i) for i in input().split()]

print(merge_lists(list1, list2))