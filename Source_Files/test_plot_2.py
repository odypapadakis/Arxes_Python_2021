import numpy as np
import matplotlib.pyplot as plt

n = [1,2,3,4,5,]
s = [i**2 for i in n]
line = plt.bar(n,s)
plt.xlabel('Number')
plt.ylabel("Square")

for i in range(len(s)):
    plt.annotate(str(s[i]), xy=(n[i],s[i]), ha='center', va='bottom')

plt.show()