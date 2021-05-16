
import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot()

ax.set_title('Nights Spent at tourist accommodation establishments\n' + ' GREECE')
ax.set_ylabel('People')
# The values to be plotted are stored below
years = ['2016', '2017', '2018', '2019']
vis_foreign = [5, 10, 15, 20]
vis_total = [25, 32, 34, 45]

# Return evenly spaced values based on the length of the list supplied
x = np.arange(len(years))  # the label locations
width = 0.2  # the width of the bars

# The two bars are created
rect1 = ax.bar(x - width/2, vis_foreign, width, label='Non Residents')
rect2 = ax.bar(x + width/2, vis_total, width, label='Total')

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
