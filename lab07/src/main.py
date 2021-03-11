import datetime
import random
import time

Registered = []


def my_time(func):
    """
    Декоратор для відстежування часу початку та завершення виконання програми
    (використовуйте модуль datetime); для симуляції довгих обчислень
    можна використовувати sleep().

    :param func: Функція, яку обгортує декоратор
    :return: Повертає функцію-"обгортку"
    """
    def wrapper(arg):
        """
        Функція-"обгортка"
        :param arg: Аргумент, який приймає основна(декорована) функція
        """
        beg_time = datetime.datetime.now()
        func(arg)
        end_time = datetime.datetime.now()
        t = end_time - beg_time
        return t
    return wrapper


def my_decorator(func):
    """
    Декоратор для декількох запусків функції у разі її неуспішного виконання

    :param func: Функція, яку обгортує декоратор
    :return: Повертає функцію-"обгортку"
    """
    def wrapper():
        """
        Функція-"обгортка"

        """
        s = False
        while not s:
            s = func()
    return wrapper


def decorator_reg(func):
    def wrapper(*arguments):
        function = func(*arguments)
        #Registered
        i = 0
        for i in range(len(Registered)):

            if func.__name__ == Registered[i]:
                return function
            i = i + 1
        Registered.append(func.__name__)
        return function
    return wrapper


@decorator_reg
def palindrome(pal):
    """
    Визначити, чи є послідовності символів поліандром

    :param pal: Послідовність символів
    """
    p = True
    time.sleep(1)
    count = int(len(pal)/2)
    for i in range(0, count):
        if pal[i] != pal[-(i+1)]:
            print("String is not palindrome")
            p = False
            break
    if p:
        print("String is palindrome")


def quicksort(nums):
    """
    Швидке сортування

    :param nums: Список з вхідними даними
    :type nums: list
    :return: Повертає відсортований список
    """
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


@decorator_reg
def my_func():
    mas = [True, False]
    f = random.choice(mas)
    if not f:
        print("Function executed wrongly")
    else:
        print("Function executed correctly")
    return f


def main():
    nums = [4, 6, 8, 20, 201, 1, 508, 64, 11, 8, 101, 6, 36]
    print("List before sorting: ")
    print(nums)
    print("List after sorting: ")
    print(quicksort(nums))
    pal = "A2BCCCCB2A"
    palindrome_decorated = my_time(palindrome)
    t = palindrome_decorated(pal)
    print(f"Time of executing: {t}")
    my_func_decorated = my_decorator(my_func)
    my_func_decorated()
    print(f"Registered: {Registered}")


if __name__ == "__main__":
    main()
