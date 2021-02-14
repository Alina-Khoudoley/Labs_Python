import random


def my_print(magazines):
    for key in magazines:
        print("Magazine #", key, " - ", magazines[key])


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

    magazines["The Guardian"] = dict()
    magazines["The Guardian"]["price"] = random.randint(20, 60)
    magazines["The Guardian"]["circulation"] = random.randrange(7000, 15000, 100)

    print("New data: ")
    my_print(magazines)

    del magazines["The Guardian"]

    print("New data: ")
    my_print(magazines)

    sl = list()
    i = 0
    print("Sorted data: ")
    for key in magazines:
        sl.append(key)
    sort_list = list(sl)
    sort_list.sort()

    for item in sort_list:
        print(item, "-", magazines[item])

    total_price = 0
    c = 0
    print("Average price of magazines whose circulation is less than 10 000:")
    for mag in sort_list:
        key = sort_list[i], "circulation"
        key1 = sort_list[i], "price"
        if magazines[key[0]][key[1]] < 10000:
            total_price += magazines[key1[0]][key1[1]]
            c += 1
        i += 1
    av_price = total_price/c
    print(av_price)


if __name__ == "__main__":
    main()
