# while , lists , strings

# odd number
def odd():
    a = 5
    while a <= 55:
        if a % 2 == 1:
            print(a)
        a += 1


def odd2():
    b = 1
    while b <= 10:
        print(b)
        b += 2

def func():
    i = 0
    while i <= 10:
        i = i + 1
        if i > 7:
            i = i + 2
    print(i)

def stars():
   s = 1
   while s < 5:
       print("*" * s)
       s += 1

def star():
    n = int(input())
    s = "*"
    while len(s) <= n:
        print(s)
        s += "*"

def s():
    i = 0
    while i < 5:
        print('*')
        if i % 2 == 0:
            print('**')
        if i > 2:
            print('***')
        i = i + 1

# print(sum(range(3,8)))

def loop():
   a = int(input())
   sum = 0
   while a != 0:
       sum += a
       a = int(input())
       print(sum)

def list():
    animals = ["cat","dog","mouse"]
    for index,value in enumerate(animals):
        print(index,value)

def num():
   a = 0
   b = 0
   while a < 10:
       print(a)
       b += a
       a += 1
   print(b)



def task1():
    s = 0
    a = int(input())
    while a != 0:
        s += a
        a = int(input())
    print(s)


# a = int(input())
# b = int(input())
# d = 1
# while d%a!=0 or d%b!=0:
#     d += 1
# print(d)


# while True:
#     a = int(input())
#     if a <= 10:
#         continue
#     elif a >= 100:
#         break
#     print(a)

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end='')
#     print()

