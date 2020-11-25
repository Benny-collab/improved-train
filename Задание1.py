# Получение чисел от пользователя
num_1 = int(input())
num_2 = int(input())
# Случай 1 (A < B)
if num_1 < num_2:
    for i in range(num_1, num_2 + 1):
        print(i)
# Случай 2 (иные случаи)
else:
    for i in range(num_1, num_2 - 1, -1):
        print(i)