import random


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


def search_value(nums, v):
    """
    Пошук елементу за значенням

    :param nums: Список з вхідними даними
    :type nums: list
    :param v: Елемент, який потрібно знайти
    :type v: int
    """
    i = 0
    c = 0
    for n in nums:
        i += 1
        if n == v:
            print(f"Item is found at index {i-1}")
            c += 1
            break
    if c == 0:
        print("Item isn't found")


def min_elem(nums, n):
    """
    Пошук перших 𝑛 мінімальних елементів

    :param nums: Список з вхідними даними
    :type nums: list
    :param n: Кількість елементів, які потрібно знайти
    :type n: int
    """
    sl = quicksort(nums)
    min_s = ""
    for i in range(0, n):
        min_s += str(sl[i]) + ', '
    print(f'{n} first min elements are: {min_s}')


def max_elem(nums, n):
    """
    Пошук перших 𝑛 максимальних елементів

    :param nums: Список з вхідними даними
    :type nums: list
    :param n: Кількість елементів, які потрібно знайти
    :type n: int
    """
    sl = quicksort(nums)
    max_s = ""
    for i in range(1, n+1):
        max_s += str(sl[-i]) + ', '
    print(f'{n} first min elements are: {max_s}')


def average(nums):
    """
    Пошук середнього арифметичного

    :param nums: Список з вхідними даними
    :type nums: list
    """
    sum = 0
    for el in nums:
        sum += el
    av = sum/len(nums)
    print('Average of list is {:.2f}'.format(av))


def unique(nums):
    """
    Повернення списку, сформованого з початкового списку, але без повторів

    :param nums: Список з вхідними даними
    :type nums: list
    """
    un_list = list()
    for elem in nums:
        if elem not in un_list:
            un_list.append(elem)
    print(f'List with unique values: {un_list}')


def palindrome(pal):
    """
    Визначити, чи є послідовності символів поліандром

    :param pal: Послідовність символів
    """
    p = True
    count = int(len(pal)/2)
    for i in range(0, count):
        if pal[i] != pal[-(i+1)]:
            print("String is not palindrome")
            p = False
            break
    if p:
        print("String is palindrome")


def main():
    nums = [4, 6, 8, 20, 201, 1, 508, 64, 11, 8, 101, 6, 36]
    print("List before sorting: ")
    print(nums)
    print("List after sorting: ")
    print(quicksort(nums))
    v = 101
    search_value(nums, v)
    num_min = 3
    num_max = 6
    min_elem(nums, num_min)
    max_elem(nums, num_max)
    average(nums)
    unique(nums)
    pal1 = "A2BCCCCB2A"
    pal2 = "A2BCCYCCB2A"
    pal3 = "A2BXCCZB2A"
    palindrome(pal1)
    palindrome(pal2)
    palindrome(pal3)


if __name__ == "__main__":
    main()
