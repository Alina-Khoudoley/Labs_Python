import math


def data(s):
    loop = True
    while loop:
        try:
            v = float(input(s))
            loop = type(v) != float or v < 0
            if v < 0:
                raise Exception("Ви ввели неправильне число.")
        except:
            print("Ви ввели неправильне число.")
    return v


x = data("Введіть додатне число x(ціле або дробове з крапкою): ")
y = data("Введіть додатне число y(ціле або дробове з крапкою): ")

z = (math.pow(math.cos(math.radians(x)), 2) + math.pow(math.sin(math.radians(y)), 2) +
     (1 / 4) * math.pow(math.sin(math.radians(2 * x)), 2) - 1)
print("Результат =", z)

proc = 105
month = 10
scholarship = data("Введіть стипендію: ")
costs_per_month = data("Введіть витрати: ")
while costs_per_month < scholarship:
    print("Ви ввели неправильне число.")
    costs_per_month = data("Введіть витрати: ")

# total_costs = costs_per_month * (1.05 ** 10 - 1) / 0.05
total_costs = costs_per_month * ((proc * (10 ** -2)) ** month - 1) / (proc * (10 ** -2) - 1)
print(f'Позика = {math.ceil(total_costs - scholarship * 10)}')
