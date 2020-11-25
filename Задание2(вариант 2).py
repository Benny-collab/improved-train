A = int(input())
B = int(input())
for i in range(A, B + 1):
    x = i // 1000
    y = i // 100 % 10
    z = i // 10 % 10
    t = i % 10
    if x == t and y == z:
        print(i)
