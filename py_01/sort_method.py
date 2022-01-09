s = [int(i) for i in input().split()]
s.sort()
print(*s)
s.sort(reverse=True)
print(*s)