import math


def my_int_input(str_out, str_err):
    while True:
        try:
            inp = int(input(str_out))
            return inp
        except ValueError:
            print(str_err)


def my_gcd(a, b):
    if (a == 0) and (b == 0):
        return 0

    if (a == 0) or (b == 0):
        return max(a, b)

    ret = 1
    for i in range(2, min(a, b) + 1):
        if(a % i == 0) and (b % i == 0):
            ret = i
    return ret


def compare():
    for a in range(0, 1000):
        for b in range(0, 1000):
            if math.gcd(a, b) != my_gcd(a, b):
                print("Не правельный ответ a, b:", a, b)
                print("gcd:", math.gcd(a, b))
                print("my gcd: ", my_gcd(a, b))
                return
    print("Всё хорошо")


compare()
