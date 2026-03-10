import numpy as np
import matplotlib.pyplot as plt

def read_data():
    file = open("data.csv")
    next(file)
    col1 = []
    col2 = []
    col3 = []
    for line in file:
        parts = line.strip().split(",")
        col1.append(float(parts[0]))
        col2.append(float(parts[1]))
        col3.append(float(parts[2]))
    file.close()
    return np.column_stack([col1,col2,col3])

def plot_height_weight(height,weight):
    plt.scatter(height,weight)
    plt.xlabel("height")
    plt.ylabel("weight")
    plt.show()

def plot_height_weight_50(height,weight):
    plt.scatter(height[::50],weight[::50])
    plt.xlabel("height")
    plt.ylabel("weight")
    plt.show()

data = read_data()
print("Min height:", np.min(data[1]))
print("Max height:", np.max(data[1]))
print("Average height:", np.mean(data[1]))

ind_m = (data[:,0] == 1)
print(ind_m)
heights_m = data[ind_m,1]
print("Min height:", np.min(heights_m))
print("Max height:", np.max(heights_m))
print("Average height:", np.mean(heights_m))
