
# This function takes as input a list that contains:
#  A panas data frame and a sting ( title )

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter

def make_charts(cleaned_file):
    # print("**************** INSIDE CHARTS *******************************")

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
    ax.set_title(title + "\n" + ' GREECE',fontsize=14)

    years = df.columns.tolist()
    years.pop(0)

    # test = df.columns.tolist(1)

    df1 = df[(df['COUNTRY'].str.contains('EL', regex=True))]

    data_foreign = df1[(df1['COUNTRY'].str.match('FOR'))]
    data_foreign = data_foreign.values.tolist()
    data_foreign = data_foreign[0]
    data_foreign.pop(0)
    data_foreign = [int(i) for i in data_foreign]

    # print(data_foreign)
    # print(type(data_foreign))

    data_total = df1[(df1['COUNTRY'].str.match('TOTAL'))]
    data_total = data_total.values.tolist()
    data_total = data_total[0]
    data_total.pop(0)
    data_total = [int(i) for i in data_total]

    # print(data_total)
    # print(type(data_total))

    # data_foreign = [5, 10, 15, 20]
    # data_total = [25, 32, 34, 45]

    # Return evenly spaced values based on the length of the list supplied
    x = np.arange(len(years))  # the label locations
    # print(x)

    y = [*range(0,10)]
    # print(y)
    # exit(0)
    width = 0.3  # the width of the bars

    # The two bars are created
    rect1 = ax.bar(x - width / 2, data_foreign, width, label='Non Residents')
    rect2 = ax.bar(x + width / 2, data_total, width, label='Total')




    ax.set_facecolor("gainsboro")
    # Ads the label on top of each bar
    asdf = mtick.StrMethodFormatter("{x:,.0f}")
    # ax.get_yaxis().set_major_formatter(
    #     mtick.FuncFormatter(lambda x, p: format(int(x), ',')))
    # ax.bar_label(rect1, padding=2,fmt = '%d')

    def millions2(x, pos):
        # 'The two args are the value and tick position'
        return '%1.9fM' % (x * 1e-1)
    # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc
    formatter2 = FuncFormatter(millions2)

    ax.bar_label(rect1, padding=5,fmt = "%d",color = '#1f77b4',backgroundcolor = '0.8', rotation = 10,size = 9 )
    # ax.bar_label(hbars, labels=['±%.2f' % e for e in error],padding=8, color='b', fontsize=14)
    ax.bar_label(rect2, padding=5,fmt = '%d',color = '#ff7f0e',backgroundcolor = '0.8', rotation = 10,size = 9)




    # Where on the graph to place X axis ticks
    ax.set_xticks(x)
    # ax.set_yticks(y)

    # Source for labels to attach to each tick
    ax.set_xticklabels(years)

    ax.set_ylabel('People',fontsize=16)
    ax.set_xlabel('YEAR', fontsize=16)

    fmt = '%d'
    fmt2 = 'num:,%d'
    tick = mtick.FormatStrFormatter(fmt2)
    # ax.get_yaxis().set_major_formatter(fmt)

    def millions(x, pos):
        # 'The two args are the value and tick position'
        return '%1.1fM' % (x * 1e-6)
    # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc
    formatter = FuncFormatter(millions)
    ax.get_yaxis().set_major_formatter(formatter)

    # StrMethod formatter
    # setup(axs1[1], title="StrMethodFormatter('{x:.3f}')")
    # ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    # ax.rect1.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))



    # ax.yaxis.set_major_formatter('{x} m')

    # Show a legend
    ax.legend()

    plt.show()