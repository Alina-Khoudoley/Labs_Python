import os
from abc import ABC, abstractmethod
from datetime import date


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
        # self.price = int(total_price)
        return int(total_price)

    def __str__(self):
        if self.is_auto:
            s = "automatic"
        else:
            s = "manual"
        return f"Brand: {self.brand}, model: {self.model}, transmission: {s}, price: {self.total_price()}, " \
               f"year: {self.year}, engine volume: {self.volume}, number of horsepower: {self.horse_power}"

    def __repr__(self):
        if self.is_auto:
            s = "automatic"
        else:
            s = "manual"
        return f"Brand: '{self.brand}', model: '{self.model}', transmission: '{s}', price: '{self.total_price()}', " \
               f"year: '{self.year}', engine volume: '{self.volume}', number of horsepower: '{self.horse_power}'"


class Person:
    def __init__(self, surname, name, age):
        self.__surname = surname
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)

    @abstractmethod
    def greeting(self):
        pass

    @abstractmethod
    def conclude_contract(self):
        pass

    @classmethod
    def from_birth_year(cls, surname, name, year):
        return cls(surname, name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


class Employee(Person):
    kind = 'person'

    def __init__(self, surname, name, age, position, salary):
        Person.__init__(self, surname, name, age)
        self.position = position
        self.salary = salary

    def greeting(self):
        print(f'Hello, my name is {self.name} and I am a {self.position} of this car rental service!')

    def conclude_contract(self):
        print('Contract is concluded!')


class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, new_list):
        self.new_list = new_list
        self.counter = 0

    def __next__(self):
        if self.counter < len(self.new_list):
            self.counter += 1
            return self.new_list[self.counter - 1].name + ' ' + str(self.new_list[self.counter - 1].salary)
        else:
            raise StopIteration


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


def simple_generator(new_list):
    c = 0
    while c < len(new_list):
        c += 1
        yield new_list[c - 1].name + ' ' + new_list[c - 1].surname


def main():
    TDI3 = Engine(3.0, 286)
    N63B44D = Engine(4.4, 530)
    PEVPS = Engine(2.0, 150)

    AudiQ7 = Car("Audi", "Q7", True, 70000, 2021, TDI3)
    BMWX6 = Car("BMW", "X6", True, 110000, 2020, N63B44D)
    MazdaCX5 = Car("Mazda", "CX-5", False, 14000, 2013, PEVPS)

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
            price = int(split_str[3].split(":")[1])
            year = int(split_str[4].split(":")[1])
            volume = float(split_str[5].split(":")[1])
            horse_power = int(split_str[6].split(":")[1])
            engines.append(Engine(volume, horse_power))
            cars.append(Car(brand, model, is_auto, price, year, engines[i]))

    for i in range(0, 3):
        print(f"Car #{i + 1}: {cars[i].brand} {cars[i].model}")
        print(cars[i])

    sales_assistant1 = Employee('Johnson', 'Mike', 28, 'sales assistant', 9500)
    sales_assistant2 = Employee('Davis', 'Liam', 33, 'sales assistant', 11000)
    person = Person.from_birth_year("M.", "Kate", 1998)
    sales_assistant2.conclude_contract()
    rental = {
        "15000": {
            "car": AudiQ7,
            "employee": sales_assistant1
        },
        "15001": {
            "car": MazdaCX5,
            "employee": sales_assistant2
        },
        "15002": {
            "car": BMWX6,
            "employee": sales_assistant1
        }
    }
    print(sales_assistant2.kind)
    print(Person.is_adult(sales_assistant1.age))
    print(person.name, person.age)
    print(f'Deal number: 15000, car: {rental.get("15000").get("car")}, employee: '
          f'{rental.get("15000").get("employee").surname} {rental.get("15000").get("employee").name}')
    print(f'Deal number: 15001, car: {rental.get("15001").get("car")}, employee: '
          f'{rental.get("15001").get("employee").surname} {rental.get("15001").get("employee").name}')
    print(f'Deal number: 15002, car: {rental.get("15002").get("car")}, employee: '
          f'{rental.get("15002").get("employee").surname} {rental.get("15002").get("employee").name}')

    employees = list()
    employees.append(sales_assistant1)
    employees.append(sales_assistant2)
    s_iter = SimpleIterator(employees)
    for i in s_iter:
        print(i)

    gen_iter = simple_generator(employees)
    print(next(gen_iter))
    print(next(gen_iter))

    with File('employees.txt', 'w') as opened_file:
        for i in range(0, len(employees)):
            opened_file.write(str(employees[i].surname) + ' ' + str(employees[i].name) + '\n')

    employees1 = list()
    with File('employees.txt', 'r') as opened_file:
        for i in range(0, len(employees)):
            employees1.append(opened_file.readline()[:-1])
            print(employees1[i])


if __name__ == "__main__":
    main()
