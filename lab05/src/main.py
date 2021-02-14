def same_letter(splitted_sent):
    num = 0
    print("Слова, що розпочинаються та закінчуються на одну й ту ж літеру: ")
    for i in range(0, len(splitted_sent)):
        if splitted_sent[i][0].lower() == splitted_sent[i][len(splitted_sent[i]) - 1].lower():
            print(splitted_sent[i])
            num += 1
    if num == 0:
        print("Такі слова не знайдено.")
    print()


def two_letters(splitted_sent):
    num = 0
    с = 0
    print("Слова, які містять дві і більше літери «е»: ")
    for i in range(0, len(splitted_sent)):
        for j in range(0, len(splitted_sent[i])):
            if splitted_sent[i][j].lower() == "e":
                с += 1
        if с >= 2:
            print(splitted_sent[i])
            num += 1
        с = 0
    if num == 0:
        print("Такі слова не знайдено.")
    print()


def one_letter(splitted_sent):
    num = 0
    print("Слова, які містять хоча б одну літеру «о»: ")
    for i in range(0, len(splitted_sent)):
        for j in range(0, len(splitted_sent[i])):
            if splitted_sent[i][j].lower() == "o":
                print(splitted_sent[i])
                num += 1
    if num == 0:
        print("Такі слова не знайдено.")
    print()


def eratosthenes_sieve(numbers):
    i = 1
    c = 1
    for num in numbers:
        while i < len(numbers):
            if numbers[i] % num == 0:
                numbers.remove(numbers[i])
                i -= 1
            i += 1
        c += 1
        i = c
    return numbers


def my_func(e):
    return len(e)


def long_word(splitted_sent):
    sort_sent = list(splitted_sent)
    sort_sent.sort(reverse=True, key=my_func)
    word = sort_sent[0]
    vowels = 'aeiou'
    i = 0
    c = 0
    num = 0
    mas = dict()
    print("\nНайдовше слово у реченні: ", word)
    print("Голосні літери у найдовшому слові: ")
    while i < len(word):
        if word[i] in vowels:
            for j in range(0, len(word)):
                if word[j] == word[i]:
                    num += 1
            c += 1
            if word[i] not in mas: mas[word[i]] = num
            num = 0
        i += 1
    print(mas)
    if c == 0:
        print("Голосних літер у найдовщому слові не знайдено.")
    splitted_sent.remove(word)
    print("Видалено найдовше слово: ", splitted_sent)


def main():
    sent = "Hello people, this is Alina. "
    sent = sent.strip()
    sent = sent.strip()
    sent = sent.replace("-", " ")
    sent = sent.replace(",", " ")
    sent = sent.replace(".", " ")
    splitted_sent = sent.split()
    same_letter(splitted_sent)
    two_letters(splitted_sent)
    one_letter(splitted_sent)
    print()

    numbers = list(range(2, 1001))
    s = eratosthenes_sieve(numbers)
    s.sort(reverse=True)
    print(
    "Множина простих цілих чисел в порядку спадання з діапазону від 2 до 1000, використовуючи метод решета Ератосфена: ")
    print(s)

    long_word(splitted_sent)
    print()


if __name__ == "__main__":
    main()
