import math

x = float(input("Введіть число x: "))
while x != float and x<0:
    input("Ви ввели неправильне число")

y = float(input("Введіть число y: "))
z = (math.pow(math.cos(math.radians(x)), 2) + math.pow(math.sin(math.radians(y)), 2) +
     (1 / 4) * math.pow(math.sin(math.radians(2 * x)), 2) - 1)
print("Результат =", z)
