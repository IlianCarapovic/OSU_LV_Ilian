import numpy as np
import matplotlib.pyplot as plt

black = np.zeros((50,50))
white = np.ones((50,50))

top = np.hstack((black,white))
bottom = np.hstack((white,black))

matrix = np.vstack((top,bottom))

plt.figure()
plt.imshow(matrix, cmap="gray")
plt.show()