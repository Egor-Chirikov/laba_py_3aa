import math


def my_float_input(str_out, str_err):
    while True:
        try:
            inp = float(input(str_out))
            return inp
        except ValueError:
            print(str_err)


angle = my_float_input("Введите угол в градусах: ", "!!Угол - это целое число или десятичная дробь через точку!!")
print("cos(", angle, ")= ", math.cos(angle), sep="")
print("sin(", angle, ")= ", math.sin(angle), sep="")
print("tan(", angle, ")= ", math.tan(angle), sep="")
