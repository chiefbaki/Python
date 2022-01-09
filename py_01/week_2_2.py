# Именованные переменные
def foo(x,y,z):
    return 100*x + 10*y + 1*z

def bar(args):
    for i in args:
        print(args)

print(foo(x= 1,z=3,y=2))