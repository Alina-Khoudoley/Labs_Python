import codecs


def first_line(s1, s2):
    with codecs.open('text.txt', encoding='utf-8', mode='r') as opened_file:
        line = opened_file.readline()
    symbols = line[s1:s2]
    return symbols


def second_line():
    file = codecs.open('text.txt', encoding='utf-8', mode='r')
    i = 0
    try:
        file.readline()
        s = file.readline()
    except ValueError:
        print("Error")
    finally:
        file.close()
    return s[0]


def n_line(k, n):
    with codecs.open('text.txt', encoding='utf-8', mode='r') as opened_file:
        for i in range(0, n-1):
            opened_file.readline()
        line = opened_file.readline()
    return line[k]


def number_symbols():
    with codecs.open('text.txt', encoding='utf-8', mode='r') as opened_file:
        text = opened_file.read()
    new_text = text.replace(" ", "")
    new_text = new_text.replace(" ", "")
    new_text = new_text.replace(",", "")
    new_text = new_text.replace(".", "")
    new_text = new_text.replace("-", "")
    new_text = new_text.replace(":", "")
    new_text = new_text.replace(";", "")
    new_text = new_text.replace("\r", "")
    new_text = new_text.replace("\n", "")

    with open("result.txt", "w") as somefile:
        somefile.write(str(len(new_text)))
    return len(new_text)


def main():
    s1 = 10
    s2 = 18
    symbols = first_line(s1, s2)
    print(f'Символи з s1-го по s2-й в першому рядку: {symbols}')
    first_symbol = second_line()
    print(f'Перший символ другого рядка: {first_symbol}')
    k = 15
    n = 4
    k_symb = n_line(k, n)
    print(f'{k}-й символ {n}-го рядка: {k_symb}')
    n = number_symbols()
    print(f'Кількість символів у файлі, окрім пробілів та символів пунктуації: {n}')
    with open('result.txt', 'r') as new_file:
        s = new_file.readline()
        print(f'Читаємо з файлу: {s}')


if __name__ == "__main__":
    main()
