dict1 = {
    'house' : 'дом',
    'car': 'машина',
    'cat': 'кошка'
}

dict2 = {
    'room': 'комната',
    'floor': 'этаж'
}

d = {**dict1, **dict2}


d1 = {'kg': '+996', 'ru': '+7', 'kz': '+8'}
for i, j in range(len(d1)):
    print(i, j)