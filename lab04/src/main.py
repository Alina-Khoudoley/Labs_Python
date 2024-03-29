import random


def my_print(magazines):
    for key in magazines:
        print("Magazine \"", key, "\" - ", magazines[key])


def av_price(key_list, magazines):
    total_price = 0
    i = 0
    c = 0
    print("Average price of magazines whose circulation is less than 10 000:")
    for mag in key_list:
        key = key_list[i], "circulation"
        key1 = key_list[i], "price"
        if magazines[key[0]][key[1]] < 10000:
            total_price += magazines[key1[0]][key1[1]]
            c += 1
        i += 1
    if c == 0: print("No magazine with circulation less than 10000 was found.")
    else:
        average_price = total_price / c
        print(average_price)


def main():
    magazines = {
        "Time": {
            "price": random.randint(20, 60),
            "circulation": random.randrange(7000, 15000, 100)
        },
        "Rolling Stone": {
            "price": random.randint(20, 60),
            "circulation": random.randrange(7000, 15000, 100)
        },
        "Bazaar": {
            "price": random.randint(20, 60),
            "circulation": random.randrange(7000, 15000, 100)
        },
        "Vogue": {
            "price": random.randint(20, 60),
            "circulation": random.randrange(7000, 15000, 100)
        },
        "WSJ": {
            "price": random.randint(20, 60),
            "circulation": random.randrange(7000, 15000, 100)
        },
    }

    my_print(magazines)

    magazines["The Guardian"] = {
            "price": random.randint(20, 60),
            "circulation": random.randrange(7000, 15000, 100)
        }
    #magazines["The Guardian"]["price"] = random.randint(20, 60)
    #magazines["The Guardian"]["circulation"] = random.randrange(7000, 15000, 100)

    print("New data after adding one element: ")
    my_print(magazines)

    del magazines["The Guardian"]

    print("New data after deleting one element: ")
    my_print(magazines)

    sl = list()
    i = 0
    k = 0
    v = 0
    print("Sorted data by alphabet: ")
    for name, magazine in sorted(magazines.items(), key=lambda x: x[0]):
        print(name, magazine)

    #sorted(magazines.items(), key=lambda item: item[1])
    # for key in magazines:
    #     sl.append(key)
    # sort_list = list(sl)
    # sort_list.sort()

    # for item in sort_list:
    #     print(item, "-", magazines[item])

    key_list = list(magazines.keys())
    av_price(key_list, magazines)


if __name__ == "__main__":
    main()
