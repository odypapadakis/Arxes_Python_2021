
# This function takes as input a list that contains:
#  A pandas data frame and a sting ( title ) and the original string
# [dataframe,local_name,original_name]

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter





def make_charts_2(cleaned_file,ax_i,ax2_i):

    ax = plt.subplot(2, 2, ax2_i+1)
    #  The list of country codes the data will be plotted for
    country_code = ['EL', 'ES']

    # The equivalent names for the above country codes
    country_name = ['Greece', 'Spain']



    df = cleaned_file[0]

    # Set the plot title as the original file name
    plot_title = cleaned_file[2]

    # ax = plt.sublot()

    # set the subplot background color
    ax.set_facecolor("gainsboro")

    # Set the label for the y axis
    ax.set_ylabel('People', fontsize=14)

    # Set the label for the x axis
    ax.set_xlabel('YEAR', fontsize=14)

    # Get the names of all the columns into a list
    # ( will be used to title each bar for the bar plot )
    years = df.columns.tolist()
    # drop the first column  from the list, as it is a title for the first column
    years.pop(0)

    # Return evenly spaced values based on the length of the list supplied
    x = np.arange(len(years))  # the label locations

    # Place ticks on the x axis, on the evenly spaced values
    ax.set_xticks(x)

    # Source for labels to attach to each tick is the years
    ax.set_xticklabels(years)

    # Keep only the rows that have the country column ends with  the country code we want
    # For example : keep only the rows in which the country column ends with 'EL'
    df1 = df[(df['COUNTRY'].str.endswith(country_code[ax_i]))]

    #
    ax.set_title(plot_title + "\n" + country_name[ax_i], fontsize=14)

    # Keep only the row that have the country column BEGIN with FOR
    # To keep the foreigners = non residents
    data_foreign = df1[(df1['COUNTRY'].str.startswith('FOR'))]
    # make the
    data_foreign = data_foreign.values.tolist()
    data_foreign = data_foreign[0]
    data_foreign.pop(0)
    data_foreign = [int(i) for i in data_foreign]

    # ----- Code to keep the total number of visitors ---

    # Keep in a dataframe only the row that has the country column that begins with TOTAL
    # To keep the total number of visitors
    data_total = df1[(df1['COUNTRY'].str.startswith('TOTAL'))]

    # Convert the  dataframe into a list of lists
    data_total = data_total.values.tolist()

    #  Keep the only item of the list
    data_total = data_total[0]

    # Delete the first item of the list, which is the country code and data type ( FOR|TOTAL)
    data_total.pop(0)

    # Make the list of strings into a list of integers
    data_total = [int(i) for i in data_total]

    width = 0.3  # the width of the bars of the plot

    # The two bars are created
    rect1 = ax.bar(x - width / 2, data_foreign, width, label='Non Residents')
    rect2 = ax.bar(x + width / 2, data_total, width, label='Total')

    #  The labels for the two bars are created
    ax.bar_label(rect1, padding=5, fmt="%d", color='#1f77b4', backgroundcolor='0.8', rotation=10, size=9)
    ax.bar_label(rect2, padding=5, fmt='%d', color='#ff7f0e', backgroundcolor='0.8', rotation=10, size=9)

    # Create the fromatting for the vertical axis
    # This code was taken from stackoverflow because I was frustrated with formatting
    # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc
    def millions(x, pos):
        # 'The two args are the value and tick position'
        return '%1.1fM' % (x * 1e-6)

    formatter = FuncFormatter(millions)

    # Set the formatting for the vertical axis
    ax.get_yaxis().set_major_formatter(formatter)

    # Show a legend
    ax.legend()



def make_charts(in_file):
    print(in_file)
    # fig, ax = plt.subplots(3, sharex=True)
    # fig.suptitle('Sharing both axes')


    make_charts_2(in_file[0], 0 , 0)
    make_charts_2(in_file[1], 0 , 1)
    make_charts_2(in_file[0], 1 , 2)
    make_charts_2(in_file[1], 1 , 3)
    # country_code = ['EL', 'ES']
    # country_name = ['Greece', 'Spain']

    plt.show()