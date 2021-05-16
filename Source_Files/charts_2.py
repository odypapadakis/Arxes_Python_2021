import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num
import datetime

# # This is to see the plot inside the notebook
# %matplotlib inline

# x = list(range(0,10))
# y = list(range(-10,0))
#
# plt.plot(x,y)
# plt.show()

# a = [0,-100,25,67,-323]
# b = [0,3,7,3,9]
#
# plt.plot(a,b,marker = 'o',color = 'r')
# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.show()


# N = 4
# ind = np.arange(N)
# #plot 1:
# years = np.array(["2016", "2017", "2018", "2019"])
# a_for = np.array([1, 10, 12, 18])
# b_total = np.array([5, 20, 30, 35])
# width = 0.35
#
# #the figure has 1 row, 2 columns, and this plot is the first plot.
# plt.subplot(1, 2, 1)
# plt.title("Spain")
#
# plt.bar(x,y,width)
#
#
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(1, 2, 2)
# plt.title("Greece")
# plt.bar(x,y,width)
#
#
# plt.suptitle("Nigths spent At tourist Accomodation establisments")
# plt.show()



# N = 4
# ind = np.arange(N)
#
#

# width = 0.35
#
# plt.title("Spain")
#
# # plt.bar(years,a_for,width)
#
# ax = plt.subplot(111)
# ax.bar( years, y,  color='b', align='center')
# ax.bar( years+0.2, z,  color='g', align='center')
#
# ax.xaxis()


# x = [
#     datetime.datetime(2011, 1, 4, 0, 0),
#     datetime.datetime(2011, 1, 5, 0, 0),
#     datetime.datetime(2011, 1, 6, 0, 0)
# ]
# print(type(x))
# print(x)
#
# x = date2num(x)
# print(type(x))
# print(x)

# x = np.array([2011.,2012.,2013.])
# y = [1, 2, 3]
# z = [4, 5, 6]

# x1 = np.array([2016, 2017, 2018, 2019])
# x2 = ['aaa', 'bbb', 'ccc', 'ddd']
# x = np.arange(len(x2))
#
# y1 = np.array([1, 10, 12, 18])
# y2 = np.array([5, 20, 30, 35])
#
# ax = plt.subplot(111)
#
# ax.set_ylabel('People')
# ax.set_ylabel('Year')
#
# ax.bar(x-0.1, y1, width=0.2, color='b', align='center')
# ax.bar(x+0.1, y2, width=0.2, color='g', align='center')
#
# # ax.xaxis_date()
#
# plt.show()



# plt.suptitle("Nigths spent At tourist Accomodation establisments")
# plt.show()



years = ['2016', '2017', '2018', '2019']
vis_foreign = [5, 10, 15, 20]
vis_total = [25, 32, 34, 45]

x = np.arange(len(years))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, vis_foreign, width, label='Non Residents')
rects2 = ax.bar(x + width/2, vis_total, width, label='Total')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('People')
ax.set_title('Nigths Spent at tourist accomodation establishments\n'+ ' GREECE')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

# Ads the label on top of each bar
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()