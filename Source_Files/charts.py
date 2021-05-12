import matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def draw_charts():
    print(matplotlib.__version__)

    # xpoints = np.array([0, 6])
    # ypoints = np.array([0, 250])

    # plt.plot(xpoints, ypoints)

    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
    myexplode = [0.2, 0, 0, 0]
    mycolors = ["red", "yellow", "pink", "black"]

    plt.pie(y,labels = mylabels, startangle = 90, explode = myexplode,colors = mycolors)
    plt.legend()
    plt.show()

    # # Three lines to make our compiler able to draw:
    # import sys
    #
    # matplotlib.use('Agg')
    #
    # y = np.array([35, 25, 25, 15])
    #
    # plt.pie(y)
    # plt.show()
    # plt.savefig(sys.stdout.buffer)
    # sys.stdout.flush()