from matplotlib import pyplot as plt
import plotly as ply
import plotly.graph_objs as go
import numpy


def plot_1():
    x = numpy.linspace(0, 5, num=300)
    y1 = -5*numpy.cos(10*x)*numpy.sin(3*x)/(x**x)

    fig, ax = plt.subplots()
    ax.plot(x, y1, color="red", label="Y(x)=-5*cos(10*x)*sin(3*x)/(x^x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc='lower left')
    plt.show()

    fig.savefig('plot.png')


def plot_2():
    r_x = numpy.linspace(1, 10, num=1000)

    pl = go.Scatter(
        x=r_x,
        y=r_x**(numpy.sin(10*r_x)),
        mode='lines',
        name='lines'
    )
    data = [pl]
    y = r_x**(numpy.sin(10*r_x))
    ply.offline.plot(data, filename='plot.html')
    plt.plot(r_x, y)
    plt.savefig("plot.pdf")


if __name__ == '__main__':
    plot_1()
    plot_2()
