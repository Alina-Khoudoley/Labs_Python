Лабораторна робота №13-14
Збір даних з веб-документів за допомогою Python. Робота з API. Бібліотека Pandas

Завдання
***Загальне завдання:***

Реалізуйте програму, яка для заданих сайтів отримує інформацію. Використати API та парсинг html сторінок за допомогою Beautiful Soup. Порівняти два підходи. Обробити та зберегти інформацію у .csv файл використовуючи Pandas.
Перетворити за необхідності код у скрипт та додати автоматичний запуск на виконання (наприклад, кожні 5 хвилин).

***Варіант №4***
https://ua.jooble.org/
А) Використовуючи API:
Для заданих запитів (наприклад Python, Java) та дат отримати вакансії (назва, заробітна плата, опис, компанія, локація).
Б) Використовуючи Beautiful Soup:
Отримати всі поточні вакансії із запитом Data Scientist та заробітною платою від 16.000 гривень. 
Приклад посилання: https://ua.jooble.org/SearchResult?ukw=data%20scientist.


Алгоритм виконання завдання:
- Для використання REST API потрібно відправити HTTP POST запит за адресою https://ua.jooble.org/api/<API KEY>.
- Ключ отримуємо після заповнення форми.  
- Задаємо дані для пошуку: посада - Senior Python, локація - Київ, зарплата - 120000.
- Використовуємо функцію eval (), що виконує код, переданий їй у вигляді рядка. Заносимо дані у змінну a.
- Виводимо на екран порядковий номер вакансії та її опис: назву, зарплату, короткий опис, компанію, локацію.
- Використовуючи Beautiful Soup: отримуємо всі поточні вакансії із запитом Data Scientist та заробітною
  платою від 16.000 гривень.
- За html-тегами та назвами класів витягуємо потрібну нам інформацію з html файлу.
- Заносимо у змінні дані про назву, зарплату, компанію та локацію.  
- Записуємо у файл *pars.csv* дані про назву, зарплату, компанію та локацію.
- Зчитуємо дані з файлу та виводимо на екран.


Приклад роботи програми
> Job №1 <br>
> Senior python developer 5 000 - 6 500 $ Eagle Genomics is looking for a , Senior Python , Developer <br>
> ▪️Salary:  $5000 - $6500 <br> 
> ▪️Full Time jobs ! <br>
> ▪️Ukraine - Kyiv - Office <br>
> ▪️Experience:  from 5 years <br>
> ▪️English:  Upper Intermediate <br> 
>  Requirements <br> 
> ▫️5+ y. in software development <br> 
> ▫️exp. with Python,  Docker,  CI - must <br> 
> MORE...&nbsp; Київ <br>  <br> 
> Job №2 <br> 
> Senior Python/Django Backend Developer 5 000 $ , Senior  Python/, Django Backend Developer <br> 
> Requirements:  <br> 
> 4 + years of Python engineering experience development experience,  including familiarity with Python 3 (we use 2.7 and 3.6). <br> 
> Fluency working with Django. You’ll have to maintain old Django 1.6 project (not actively...&nbsp; Greenwich Group Київ <br> 
> ['Data Engineer', '4 000 - 5 000 $', 'TechHunt', 'Віддалено'] <br> <br>
> ['Junior Python developer', '600 - 800 $', 'Simporter', 'Київ'] <br> 
> ['Machine Learning Engineer (remote / office)', '4 000 - 4 500 $', 'IT Recruitment Solutions (ITRS.ua) ®', 'Київ'] <br> 