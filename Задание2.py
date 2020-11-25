num1 = int(input())
num2 = int(input())
for i in range(num1, num2):
    ii = str(i)
    if int(i / 100) == int(ii[3] + ii[2]):
        print(i)