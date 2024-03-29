Лабораторна робота №1-2
Налаштування середовища розробки програм мовою Python. Змінні, оператори, цикли у Python

Завдання №1
Обчислити вираз. Дані вводяться користувачем у консолі Python (за допомогою input()). 
Передбачити можливі помилки, вивести відповідне повідомлення.

***Варіант №6***
z=cos(x)^2+sin(y)^2+(1/4)*sin(2x)^2-1

Алгоритм виконання першого завдання:
- Користувач вводить дані за допомогою методу *input()*. Потім перевіряємо введені дані на валідність 
  за допомогою власної функції **data**. Якщо введені дані вірні, записуємо їх у змінну *х*.
- Таким же чином записуємо змінну *y*.
- Обчислюємо заданий індивідуальний вираз. Метод *pow()* обчислює квадрат числа. Методи *cos()* та *sin()* 
  обчислюють відповідно косинус та синус. Метод *radians()* конвертує значення у градусах у значення в радіанах.
- Виводимо на екран **результат** обчислення виразу за допомогою методу *print()*.

Завдання №2
Реалізувати програму для заданого завдання.

***Варіант №6***
Щомісячна стипендія студента становить A грн., а витрати на
проживання перевищують стипендію й становлять В грн. на місяць. Ріст цін
щомісяця збільшує витрати на 5%. Складіть програму розрахунку суми
грошей, яку необхідно одноразово запозичити, щоб можна було прожити
навчальний рік (10 місяців), використовуючи тільки ці гроші й стипендію.

Алгоритм виконання другого завдання:
- Користувач вводить дані за допомогою методу *input()*. Потім перевіряємо введені дані на валідність 
  за допомогою власної функції **data**. Якщо введені дані вірні, записуємо їх у змінну стипендії *scholarship*.
- Таким же чином записуємо змінну витрат на місяць *costs_per_month*.
- Використовуючи формулу **геометричної прогесії** (так як щомісяця витрати збільшуються на 5%), обчислюємо
загальні витрати на *10 місяців*.
- Від отриманої суми віднімаємо сумарну стипендію за 10 місяців.
- Виводимо на екран **результат** - суму, яку потрібно одноразово запозичити, якої вистачить на весь навчальний рік.

Приклад роботи програми
> Введіть додатне число x(ціле або дробове з крапкою):<br>
> 55 <br>
> Введіть додатне число y(ціле або дробове з крапкою):<br>
> 120 <br>
> Результат = **0.29974548372703813** <br>
> Введіть стипендію: <br> 
> 1200 <br>
> Введіть витрати: <br>
> 3500 <br>
> Позика = **32023** <br>
