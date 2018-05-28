import matplotlib.pyplot as plt
import matplotlib as mpl

def generate_plot(filename, f_x, f_y, title, x_legend, y_legend):

    fig = plt.figure()

    fig.set_size_inches(17,10)

    plt.title(title)

    plt.xlabel(x_legend)
    plt.ylabel(x_legend)

    plt.grid()
    plt.plot(f_x, f_y)

    plt.show()
    
    fig.savefig('./results/{}.png'.format(filename), dpi=fig.dpi)
