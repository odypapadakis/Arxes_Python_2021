import matplotlib

def draw_charts()
    # Three lines to make our compiler able to draw:
    import sys
    import matplotlib
    matplotlib.use('Agg')

    import matplotlib.pyplot as plt
    import numpy as np

    y = np.array([35, 25, 25, 15])

    plt.pie(y)
    plt.show() 
