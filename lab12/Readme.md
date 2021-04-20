#Лабораторна робота №12
##Ітератори та генератори Python

###Завдання
***Загальне завдання:***

Використовуючи попередню ЛР розширити її таким чином:
1. Додати ітератор на основі класу, що зможе працювати із класами-наслідниками.
2. Додати генератор у класс-наслідник.
3. Оновити метод зчитування із файла, написати власний менеджер контексту, що буде здатний зчитувати із файлу дані та 
   повертати список об’єктів класу-наслідника.


####Алгоритм виконання завдання:
- Використовуємо попередню лабораторну роботу, прикладну область сервісу аренди авто.
- Створюємо клас, що є ітератором **SimpleIterator**, що містить методи iter, init та next, що повертає ім'я та зарплатню співробітника.
- Створюємо метод-генератор **simple_generator**, що містить *yield*.
- Створюємо власний менеджер контексту *File*.
- Зчитуємо із файлу дані та повертаємо список об’єктів класу-наслідника.


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
> Mike 9500 <br> 
> Liam 11000 <br> 
> Mike Johnson <br> 
> Liam Davis <br> 
> Johnson Mike <br> 
> Davis Liam <br> 