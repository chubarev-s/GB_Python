# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


a = input("Введите трёхзначное число: ")
if len(a) > 3:
    print("Введите трёхзначное число!")
elif len(a) < 3:
    print("Введите трёхзначное число!")
else : 
    a1 = int(a[0])
    a2 = int(a[1])
    a3 = int(a[2])
    s = a1 + a2 + a3
    print(f"Сумма цифр: {s}")