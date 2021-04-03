import os


class Engine:
    def __init__(self, volume, horse_power):
        self.volume = volume
        self.horse_power = horse_power


class Car:
    def __init__(self, brand, model, is_auto, price, year, engine):
        self.brand = brand
        self.model = model
        self.is_auto = is_auto
        self.price = price
        self.year = year
        self.volume = engine.volume
        self.horse_power = engine.horse_power
        self.total_price()

    def year_price(self):
        if self.year <= 2010:
            price = self.price * 0.9
        elif 2010 < self.year <= 2015:
            price = self.price
        else:
            price = self.price * 1.2
        return price

    def total_price(self):
        price = self.year_price()
        if self.is_auto:
            total_price = price * 1.2
        else:
            total_price = price
        #self.price = int(total_price)
        self.price = total_price
        return int(total_price)

    def __str__(self):
        if self.is_auto:
            s = "automatic"
        else:
            s = "manual"
        return f"Brand: {self.brand}, model: {self.model}, transmission: {s}, price: {self.price}, " \
               f"year: {self.year}, engine volume: {self.volume}, number of horsepower: {self.horse_power}"

    def __repr__(self):
        if self.is_auto:
            s = "automatic"
        else:
            s = "manual"
        return f"Brand: '{self.brand}', model: '{self.model}', transmission: '{s}', price: '{self.price}', " \
               f"year: '{self.year}', engine volume: '{self.volume}', number of horsepower: '{self.horse_power}'"


def main():
    TDI3 = Engine(3.0, 286)
    N63B44D = Engine(4.4, 530)
    PEVPS = Engine(2.0, 150)

    AudiQ7 = Car("Audi", "Q7", True, 70000, 2021, TDI3)
    BMWX6 = Car("BMW", "X6", True, 110000, 2020, N63B44D)
    MazdaCX5 = Car("Mazda", "CX-5", False, 14000, 2013, PEVPS)

    print(repr(AudiQ7))
    print(repr(BMWX6))
    print(repr(MazdaCX5))

    with open('cars.txt', 'w') as opened_file:
        opened_file.write(AudiQ7.__str__() + "\n")
        opened_file.write(BMWX6.__str__() + "\n")
        opened_file.write(MazdaCX5.__str__() + "\n")

    try:
        os.path.exists('cars.txt')
    except FileNotFoundError:
        print("File doesn't exists")
    else:
        file = open('cars.txt', 'r')
        cars_list = file.readlines()

    if cars_list:
        cars, engines = [], []
        for i in range(0, 3):
            str1 = cars_list[i]
            new_str = str1.replace(" ", "")
            split_str = new_str.split(",")
            brand = split_str[0].split(":")[1]
            model = split_str[1].split(":")[1]
            is_auto = bool(split_str[2].split(":")[1])
            price = int(float(split_str[3].split(":")[1]))
            year = int(split_str[4].split(":")[1])
            volume = float(split_str[5].split(":")[1])
            horse_power = int(split_str[6].split(":")[1])
            engines.append(Engine(volume, horse_power))
            cars.append(Car(brand, model, is_auto, price, year, engines[i]))

    for i in range(0, 3):
        print(f"Car #{i+1}: {cars[i].brand} {cars[i].model}")
        print(cars[i])


if __name__ == "__main__":
    main()
