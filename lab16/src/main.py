import datetime
import plotly as ply
from matplotlib import pyplot as plt
import numpy
import sys
import logging
import plotly.graph_objs as go


def plot_1(number):
    x = numpy.linspace(0, 5, number)
    y1 = -5 * numpy.cos(10 * x) * numpy.sin(3 * x) / (x ** x)

    fig, ax = plt.subplots()
    ax.plot(x, y1, color="red", label="Y(x)=-5*cos(10*x)*sin(3*x)/(x^x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc='lower left')
    plt.show()

    fig.savefig('plot.png')


def plot_2(number):
    r_x = numpy.linspace(1, 10, number)

    pl = go.Scatter(
        x=r_x,
        y=r_x ** (numpy.sin(10 * r_x)),
        mode='lines',
        name='lines'
    )
    data = [pl]
    y = r_x ** (numpy.sin(10 * r_x))
    ply.offline.plot(data, filename='plot.html')
    plt.plot(r_x, y)
    plt.savefig("plot.pdf")


def help():
    print("Скрипт для построения графиков\n")
    print("Использование:\n"
          "main.py [число] <аргумент>\n")
    print("Число       -          Количество точек на графике\n")
    print("Аргументы:\n"
          "-h, --help            Справка о программе\n"
          "-p1, --plot_1         Выполнение построения графика первой функции\n"
          "-p2, --plot_2         Выполнение построения графика второй функции\n")
    return 0


def log(time_1):
    logging.basicConfig(filename="sample.log", level=logging.INFO)

    logging.info(f"Working time of script: {time_1}")


args = len(sys.argv)
if args < 1:
    print("Введите как минимум один аргумент. Чтобы посмотреть справку о работе скрипта введите аргумент -h или --help")

else:
    try:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            help()
        else:
            try:
                start_time = datetime.datetime.now()
                num = int(sys.argv[1])
                if sys.argv[2] == "-p1" or sys.argv[2] == "--plot_1":
                    plot_1(num)
                elif sys.argv[2] == "-p2" or sys.argv[2] == "--plot_2":
                    plot_2(num)
                end_time = datetime.datetime.now()
                total_time = end_time - start_time
                log(total_time)
            except TypeError:
                print('Первый аргумент не верный. Введите количество точек для построения графика функции(целое число)')
                print("Введите -h или --help чтобы просмотреть справку о программе")
    except :
        print('Не верный аргумент. Попробуйте еще раз..')
