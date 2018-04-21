import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as st

gaus_dist = np.random.randn(15000)
plt.hist(gaus_dist, bins=40)
plt.title("Money flow distribution")
plt.xlabel("Money flow")
plt.ylabel("Frequency")

plt.show()
