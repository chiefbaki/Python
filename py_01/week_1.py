import math
# # def func(x):
# #     if x % 2 == 0:
# #         print("Четное")
# #     else:
# #         print("Нечетное")
# # func(10)

# x = """Hello World"""
# print(x)

# x = "Hello" + " " + str(23)
# print(x)

# формула Герона
def func(a,b,c):
    p = a + b + c / 2
    s =  math.sqrt(p*(p - a)*(p - b)*(p - c))
    print(s)
func(5,6,7)
    
# интервал
# (−15,12]∪(14,17)∪[19,+∞)

def some_func():
    x = int(input())
    if x > 0:
        if x > -15 and x <= 12:
            print(True)
        elif x > 14 and x < 17:
            print(True)
        elif x > 19 and x <= math.inf:
            print(True)
    else:
        print(False)
some_func()


