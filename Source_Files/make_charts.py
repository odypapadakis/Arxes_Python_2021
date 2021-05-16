
# This function takes as input a list that contains:
#  A panas data frame and a sting ( title )

import matplotlib.pyplot as plt
import numpy as np

def make_charts(cleaned_file):

    # print(cleaned_file)
    # print(type(cleaned_file[0]))
    # print(type(cleaned_file[1]))
    # print(type(cleaned_file[2]))

    df = cleaned_file[0]
    title = cleaned_file[2]
    ax = plt.subplot()
    ax.set_title(title + "\n" + ' GREECE')
    ax.set_ylabel('People')

    years = df.columns.tolist()
    years.pop(0)


    vis_foreign = [5, 10, 15, 20]
    vis_total = [25, 32, 34, 45]

    # Return evenly spaced values based on the length of the list supplied
    x = np.arange(len(years))  # the label locations
    width = 0.2  # the width of the bars

    # The two bars are created
    rect1 = ax.bar(x - width / 2, vis_foreign, width, label='Non Residents')
    rect2 = ax.bar(x + width / 2, vis_total, width, label='Total')

    # Ads the label on top of each bar
    ax.bar_label(rect1, padding=3)
    ax.bar_label(rect2, padding=3)

    # Where on the graph to place X axis ticks
    ax.set_xticks(x)
    # Source for labels to attach to each tick
    ax.set_xticklabels(years)

    # Show a legend
    ax.legend()

    plt.show()