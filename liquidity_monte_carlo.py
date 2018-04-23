import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as st

translation = 2
gaus_dist = np.random.randn(15000)
plt.hist(gaus_dist + translation, bins=40)
plt.title("Money flow distribution")
plt.xlabel("Money flow")
plt.ylabel("Frequency")

plt.show()
