
# This function takes as input a list that contains:
#  A panas data frame and a sting ( title )

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

def make_charts(cleaned_file):
    print("**************** INSIDE CHARTS *******************************")

    cleaned_file = cleaned_file[0]
    # print(cleaned_file)
    # print(type(cleaned_file[0]))
    # exit(0)
    # print("----------------------")
    # print(type(cleaned_file[1]))
    # print("----------------------")
    # print(type(cleaned_file[2]))
    # exit(0)

    df = cleaned_file[0]
    title = cleaned_file[2]
    ax = plt.subplot()
    ax.set_title(title + "\n" + ' GREECE')


    years = df.columns.tolist()
    years.pop(0)

    # test = df.columns.tolist(1)

    df1 = df[(df['COUNTRY'].str.contains('EL', regex=True))]

    data_foreign = df1[(df1['COUNTRY'].str.match('FOR'))]
    data_foreign = data_foreign.values.tolist()
    data_foreign = data_foreign[0]
    data_foreign.pop(0)
    data_foreign = [int(i) for i in data_foreign]

    print(data_foreign)
    # print(type(data_foreign))


    data_total = df1[(df1['COUNTRY'].str.match('TOTAL'))]
    data_total = data_total.values.tolist()
    data_total = data_total[0]
    data_total.pop(0)
    data_total = [int(i) for i in data_total]

    print(data_total)
    # print(type(data_total))



    # data_foreign = [5, 10, 15, 20]
    # data_total = [25, 32, 34, 45]

    # Return evenly spaced values based on the length of the list supplied
    x = np.arange(len(years))  # the label locations
    # print(x)

    y = [*range(0,10)]
    # print(y)
    # exit(0)
    width = 0.4  # the width of the bars

    # The two bars are created
    rect1 = ax.bar(x - width / 2, data_foreign, width, label='Non Residents')
    rect2 = ax.bar(x + width / 2, data_total, width, label='Total')

    # Ads the label on top of each bar
    ax.bar_label(rect1, padding=2,fmt = '%d')
    ax.bar_label(rect2, padding=2,fmt = '%d')

    # Where on the graph to place X axis ticks
    ax.set_xticks(x)
    # ax.set_yticks(y)

    # Source for labels to attach to each tick
    ax.set_xticklabels(years)

    ax.set_ylabel('People',fontsize=16)
    ax.set_xlabel('YEAR', fontsize=16)

    fmt = '%d'
    tick = mtick.FormatStrFormatter(fmt)
    ax.get_yaxis().set_major_formatter(tick)

    # Show a legend
    ax.legend()

    plt.show()