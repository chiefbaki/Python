# return bool values 

def is_invalid(model):
    while model != 300 or model != 400 or model != 500:
        return True
    else:
        return False
    
def is_even(num):
    return num % 2 == 0


def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

def get_next_prime(num):
    while not is_prime(num):
        num += 1 
    return num 

# n = int(input())
# print(get_next_prime(n+1))

def is_password_good(password):
    flag1 = False
    flag2 = False
    flag3 = False 
    if len(password) <= 8:
        return False
    for i in password:
        if i.isupper():
            flag1 = True 
        elif i.islower():
            flag2 = True 
        elif i.isdigit():
            flag3 = True
        
    return flag1 and flag2 and flag3

def is_one_away(word1, word2):
    if len(word1) == len(word2):
        cnt = 0
        for c in range(len(word1)):
            if word1[c] == word2[c]:
                cnt += 1
        if len(word1) - cnt == 1:
            return True
    return False

def is_palindrom(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    return text != text[::-1]
# text = input().lower()


def is_valid_password(password):
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False

    a = password[0]
    b = int(password[1])
    c = int(password[2])

    if len(password) == 3:
        flag1 = True
        if a == a[::-1]:
            flag2 = True
        for i in range(2, b+1):
            if b % i == 0:
                break
            else:
                flag3 = True
        if c % 2 == 0:
            flag4 = True
    
    return flag1 and flag2 and flag3 and flag4
# считываем данные
        
# p = input().split(':')
# print(is_valid_password(p))

def is_correct_bracket(text):
    pass


# text = input()
# print(is_correct_bracket(text))

def func():
    return 'string', 4, {1:2}, (2,3), True


# t = (1, 2, 3, 4, (10, 20))
# a, b, d, e, (f, g) = t
# print(g)
# *c, (a, b) = t
# print(*c)
# print(a)
# print(b)

def square(x):
    return x**2  

def problem(a, b):
    return a + square(b)


# объявление функции
def solve(a, b, c):
    pass

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
