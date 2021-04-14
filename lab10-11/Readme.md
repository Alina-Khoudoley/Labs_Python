#Лабораторна робота №10-11
##Наслідування та поліморфізм у Python

###Завдання
***Загальне завдання:***

Використовуючи створені класи розширити попередню ЛР таким чином:
1. Створити ієрархію класів. Додати до ієрархії класів хоча б один абстрактний клас (не менше двох абстрактних методів).
2. У похідному класі/класах (класі-насліднику) додати змінну класу (class variable). Продемонструвати різницю між змінними класу та екземпляра.
3. Додати статичні методи та методи класу.
4. Обробити можливі помилки, розробивши власну ієрархію виключень.


####Алгоритм виконання завдання:
- Використовуємо створену прикладну область сервісу аренди авто.
- Реалізуємо клас **Person**.
- Реалізуємо клас-наслідник **Employee**, що наслідується від класу Person.
- У класі-батьку Person реалізуємо два абстрактні методи *greeting* та *conclude_contract*.
- У похідному класі додаємо змінну класу **kind**.
- Додаємо статичний метод *is_adult* та метод класу *from_birth_year* у клас Person.
- Додаємо можливість зчитування та запису об’єктів у файли.
- Обробити можливі помилки при роботі з файлом.


### Приклад роботи програми
> Car #1: Audi Q7 <br>
> Brand: Audi, model: Q7, transmission: automatic, price: 145152.0, year: 2021, engine volume: 3.0, number of horsepower: 286 <br>
> Car #2: BMW X6 <br> 
> Brand: BMW, model: X6, transmission: automatic, price: 228096.0, year: 2020, engine volume: 4.4, number of horsepower: 530 <br>
> Car #3: Mazda CX-5 <br>
> Brand: Mazda, model: CX-5, transmission: automatic, price: 16800.0, year: 2013, engine volume: 2.0, number of horsepower: 150 <br>
> Contract is concluded! <br>
> person <br>
> True <br>
> Kate 23 <br>
> Deal number: 15000, car: Brand: Audi, model: Q7, transmission: automatic, price: 100800, year: 2021, engine volume: 3.0, number of horsepower: 286, employee: Johnson Mike <br>
> Deal number: 15001, car: Brand: Mazda, model: CX-5, transmission: manual, price: 14000, year: 2013, engine volume: 2.0, number of horsepower: 150, employee: Davis Liam <br>
> Deal number: 15002, car: Brand: BMW, model: X6, transmission: automatic, price: 158400, year: 2020, engine volume: 4.4, number of horsepower: 530, employee: Johnson Mike <br>