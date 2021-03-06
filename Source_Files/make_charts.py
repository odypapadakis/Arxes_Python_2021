
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# This function takes 4 inputs:
# 1) A list that contains:
#   1.1) a pandas dataframe
#   1.2) The user title
#   1.3) The original file name to be used as the subplot title
# 2) The number of the subplot
# 3) The list of country codes
# 4) The list of country names


def make_charts_2(list_in, subplot_number, country_code, country_name):

    # There will be 4 plots, in a 2 x 2  grid
    plot = plt.subplot(2, 2, subplot_number)

    # Set the plot title as the original file name
    plot_title = list_in[2]

    # Set the title of the subplot
    plot.set_title(plot_title + "\n" + country_name, fontsize=14)

    # set the subplot background color for better readability
    plot.set_facecolor("gainsboro")

    # Set the label for the y axis
    plot.set_ylabel('People', fontsize=14)

    # Set the label for the x axis
    plot.set_xlabel('YEAR', fontsize=14)

    # Get the dataframe from the list
    df = list_in[0]

    # Get the names of all the columns into a list
    # ( will be used to title each bar for the bar plot )
    years = df.columns.tolist()
    # drop the first column  from the list
    years.pop(0)

    # Return evenly spaced values based on the length of the list supplied
    # example: For 4 years, x will be [ 0 1 2 3]
    x = np.arange(len(years))  # the label locations

    # Place  ticks(labels) on the x axis, on the evenly spaced values
    plot.set_xticks(x)

    # Source for labels text  to attach to each tick is the years
    plot.set_xticklabels(years)

    # -------------   Code to keep the correct country rows  -------------

    # Keep only the rows that have the country column ends with  the country code we want
    # example : keep only the rows in which the country column ends with 'EL'
    df1 = df[(df['COUNTRY'].str.endswith(country_code))]

    # -------------   Code to keep the  number of Foreign visitors -------------

    # Keep only the row that have the country column BEGIN with FOR
    # To keep the foreigners = non residents
    data_foreign = df1[(df1['COUNTRY'].str.startswith('FOR'))]
    # Convert the  dataframe into a list of lists
    data_foreign = data_foreign.values.tolist()
    #  Keep the only item of the list
    data_foreign = data_foreign[0]
    # Delete the first item of the list, which is the country code and data type ( FOR|TOTAL)
    data_foreign.pop(0)
    # Make the list of strings into a list of integers
    data_foreign = [int(i) for i in data_foreign]

    # -------------   Code to keep the total number of visitors -------------

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
    rect1 = plot.bar(x - width / 2, data_foreign, width, label='Non Residents')
    rect2 = plot.bar(x + width / 2, data_total, width, label='Total')

    #  The labels for the two bars are created
    plot.bar_label(rect1, padding=5, fmt="%d", color='#1f77b4', backgroundcolor='0.8', rotation=10, size=9)
    plot.bar_label(rect2, padding=5, fmt='%d', color='#ff7f0e', backgroundcolor='0.8', rotation=10, size=9)

    # Create the formatting for the vertical axis
    # This code was taken from stackoverflow
    # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc
    def millions(x, pos):
        return '%1.1fM' % (x * 1e-6)
    # Create the formatting for the vertical axis
    formatter = FuncFormatter(millions)

    # Set the formatting for the vertical axis
    plot.get_yaxis().set_major_formatter(formatter)

    # Show a legend
    plot.legend()


# This function takes as input
# 1) A list of lists, each list consists of 3 items
#   1.1) A pandas data frame
#   1.2)  The user appointed name
#   1.3) The original name of the tsv file
# 2) The number of the subplot to be created
# 3) A list of country codes ['EL', 'ES']
# 4) A list of country names ['Greece', 'Spain']

def make_charts(in_list, country_codes, country_names):


    nigths_list = in_list[0]
    arrivals_list = in_list[1]

    make_charts_2(nigths_list,     1, country_codes[0], country_names[0])
    make_charts_2(nigths_list,     3, country_codes[1], country_names[1])
    make_charts_2(arrivals_list,   2, country_codes[0], country_names[0])
    make_charts_2(arrivals_list,   4, country_codes[1], country_names[1])

    plt.show()