a = [50, 32, 55, -2, -10, 40]
n = len(a)

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break

print(f'Sorted list: {a}')