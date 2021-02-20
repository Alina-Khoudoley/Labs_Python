import random


def data(s):
    loop = True
    while loop:
        try:
            v = int(input(s))
            loop = type(v) != int or v < 0
            if v < 0:
                raise Exception("Ви ввели неправильне число.")
        except:
            print("Ви ввели неправильне число.")
    return v


def prod(nl):
    i = 0
    p = 1
    while i < len(nl[1]):
        if nl[1][i] < 0:
            p *= nl[1][i]
        i += 1
    return p


def my_count(nl):
    i = 0
    c = 0
    while i < len(nl):
        if nl[i][1] % 5 != 0:
            c += 1
        i += 1
    return c


def words(splitted_list):
    i = 0
    my_list = list()
    while i < len(splitted_list):
        c = splitted_list.count(splitted_list[i])
        if c == 2:
            if not splitted_list[i] in my_list: my_list.append(splitted_list[i])
        i += 1
    if not my_list:
        print("Такі слова не знайдені.")
    else:
        print(my_list)


def main():
    n = data("Введіть кількість елементів у списку: ")
    my_list = list()
    i = 0
    while i < n:
        my_list.append(random.randint(0, 50))
        i += 1
    print(my_list)

    j = 0
    k = data("Введіть на скільки позицій вліво будуть циклічно зсунуті усі елементи списку: ")
    new_list = list(my_list)
    i = 0
    while i < len(my_list) - k:
        new_list[i] = my_list[i + k]
        i += 1

    while len(my_list) - k <= i < len(new_list):
        new_list[i] = my_list[j]
        i += 1
        j += 1
    print(new_list)

    nested_list = list()
    n = data("Введіть кількість рядків(мінімум 2): ")
    if n < 2:
        print("Ви ввели неправильне число.")
        n = data("Введіть кількість рядків(мінімум 2): ")
    m = data("Введіть кількість стовпців(мінімум 2): ")
    if m < 2:
        print("Ви ввели неправильне число.")
    i = 0
    j = 0
    while i < n:
        nested_list_s = list()
        while j < m:
            nested_list_s.append(random.randint(-10, 10))
            j += 1
        j = 0
        nested_list.append(nested_list_s)
        i += 1
    for nl in nested_list:
        for item in nl:
            print(item, end=" | ")
        print('\n')

    product = prod(nested_list)
    print(f'Добуток від’ємних елементів другого рядка: = {product}')
    c = my_count(nested_list)
    print(f'Кількість елементів в другому стовпчику, які не кратні «5»: = {c}')

    sent1 = "Hello, world world. "
    sent2 = "Hello this is Alina. "
    sent1 = sent1.strip()
    sent1 = sent1.replace("-", " ")
    sent1 = sent1.replace(",", " ")
    sent1 = sent1.replace(".", " ")
    sent2 = sent2.strip()
    sent2 = sent2.replace("-", " ")
    sent2 = sent2.replace(",", " ")
    sent2 = sent2.replace(".", " ")

    splitted_sent1 = sent1.split()
    splitted_sent2 = sent2.split()
    splitted_list = splitted_sent1 + splitted_sent2

    print("Слова, що зустрічаються один раз в обох реченнях: ")
    words(splitted_list)


if __name__ == "__main__":
    main()
