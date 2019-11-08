import matplotlib.pyplot as plt #画图工具
import pandas as pd
import numpy as np    #一个开源的Python科学计算基础库
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import axes3d,Axes3D


# 定义plot_data函数画出散点图
def plot_data(x, y):
    plt.plot(x, y, 'rx')


plt.show()

data = np.loadtxt('data1.txt', delimiter=',')  # 加载数据
X = data[:, 0]
y = data[:, 1]
m = y.size
plt.ion()
plt.figure(0)
plot_data(X, y)
