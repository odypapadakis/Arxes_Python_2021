
# This function takes as input a list that contains:
#  A pandas data frame and a sting ( title ) and the original string
# [dataframe,local_name,original_name]

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter





def make_charts(in_file):
    #  The list of country codes the data will be plotted for
    countries = ['EL', 'ES']

    # The equivalent names for the above country codes
    countries_longname = ['Greece', 'Spain']



    # asd
    cleaned_file = in_file[0]
    # print(cleaned_file)

    df = cleaned_file[0]

    # Set the plot title as the original file name
    plot_title = cleaned_file[2]
    
    ax = plt.subplot()
    
    # set the subplot background color
    ax.set_facecolor("gainsboro")

    # Set the label for the y axis
    ax.set_ylabel('People',fontsize=16)

    # Set the label for the x axis
    ax.set_xlabel('YEAR', fontsize=16)


    # Get the names of all the columns into a list
    # ( will be used to title each bar for the bar plot )
    years = df.columns.tolist()
    # drop the first column  from the list, as it is a title for the first column
    years.pop(0)


    # Keep only the rows that have the country column ends with  the country code we want
    # For example : keep only the rows in which the country column ends with 'EL'
    df1 = df[(df['COUNTRY'].str.endswith(countries[0]))]



    # country_title =
    ax.set_title(plot_title + "\n" + countries_longname[0], fontsize=14)

    # Keep only the row that have the country column BEGIN with FOR
    # To keep the foreigners = non residents
    data_foreign = df1[(df1['COUNTRY'].str.startswith('FOR'))]
    # make the
    data_foreign = data_foreign.values.tolist()
    data_foreign = data_foreign[0]
    data_foreign.pop(0)
    data_foreign = [int(i) for i in data_foreign]


    print("-------------------------")
    # Keep in the dataframe only the row that has the country column BEGIN with TOTAL
    # To keep the total number of visitors
    data_total = df1[(df1['COUNTRY'].str.startswith('TOTAL'))]
    print(data_total)
    print("-------------------------")


    # Convert the  dataframe into a list
    data_total = data_total.values.tolist()
    print(data_total)
    print("-------------------------")

    data_total = data_total[0]
    print(data_total)
    print("-------------------------")

    data_total.pop(0)
    print(data_total)
    print("-------------------------")

    data_total = [int(i) for i in data_total]
    print(data_total)
    print("-------------------------")


    # Return evenly spaced values based on the length of the list supplied
    x = np.arange(len(years))  # the label locations
    # Where on the graph to place X axis ticks
    ax.set_xticks(x)
    # Source for labels to attach to each tick is the years
    ax.set_xticklabels(years)


    width = 0.3  # the width of the bars of the plot

    # The two bars are created
    rect1 = ax.bar(x - width / 2, data_foreign, width, label='Non Residents')
    rect2 = ax.bar(x + width / 2, data_total, width, label='Total')



    ax.bar_label(rect1, padding=5,fmt = "%d",color = '#1f77b4',backgroundcolor = '0.8', rotation = 10,size = 9 )
    ax.bar_label(rect2, padding=5,fmt = '%d',color = '#ff7f0e',backgroundcolor = '0.8', rotation = 10,size = 9)







    def millions(x, pos):
        return '%1.1fM' % (x * 1e-6)
    # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc
    #  Create the fromatting for the vertical axis
    formatter = FuncFormatter(millions)

    # Set the formatting for the vertical axis
    ax.get_yaxis().set_major_formatter(formatter)

    # Show a legend
    ax.legend()

    plt.show()