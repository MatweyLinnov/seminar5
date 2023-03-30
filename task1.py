
first_num = int(input("Введите число: "))
second_num = int(input("Введите степень числа: "))


def degree(first_num, second_num):
    if second_num == 0:
        return 1

    return first_num * degree(first_num, second_num - 1)


print(degree(first_num, second_num))