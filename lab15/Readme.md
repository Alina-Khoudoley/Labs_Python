#Лабораторна робота №15
##Візуалізація даних у Python

###Завдання
***Загальне завдання:***

1. Відповідно до варіанта побудувати два графіки функцій (підписати вісі координат, додати легенду, крок обирати довільно):
 - А) Перший графік функції - за допомогою бібліотеки matplotlib; Зберегти отриманий графік у .png форматі.
 - Б) Другий графік функції – за допомогою бібліотеки plotly; Зберегти отриманий графік у .html та у .pdf форматах.

***Варіант №7***
- А) Y(x)=-5*cos(10*x)*sin(3*x)/(x^x), x=[0...5]
- Б) Y(x)=x^sin(10*x), x=[1...10]


####Алгоритм виконання завдання:
- Використовуємо бібліотеку matplotlib.
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