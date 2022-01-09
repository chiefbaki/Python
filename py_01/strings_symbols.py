def task_1():
    genome = input()
    let_g = genome.lower().count('g')
    let_c = genome.lower().count('c')
    sum = (let_c + let_g)/len(genome)*100
    print(sum)

def func():
    genome = 'AccTgg'
    p = 'cc'
    genome = genome.find(p)
    return genome

# genome = str(input())
# if genome[::-1] == genome[::-1]:
#     print('True')
# else:
#     print('False')

# s = 'qwertyuiop'
# print(s[5:2])

# task 2


