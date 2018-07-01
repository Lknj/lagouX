import numpy as np
import matplotlib.pyplot as plt

# 创建一个8*6大小的figure，并设置每英寸80个像素点
plt.figure(figsize = (8, 6), dpi = 80)

# 创建在1*1的位置创建一个subplot
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C, S = np.cos(X), np.sin(X)

# 绘制cosine/sine函数，设置颜色，line宽，线型
plt.plot(X, C, color = "blue", linewidth = 1.0, linestyle = '-')
plt.plot(X, S, color = "green", linewidth = 1.0, linestyle = '-')

# 设置X轴和Y轴范围
plt.xlim(-4.0, 4.0)
plt.ylim(-1.0, 1.0)

# 设置X轴和Y轴下标
plt.xticks(np.linspace(-4, 4, 9, endpoint = True))
plt.yticks(np.linspace(-1, 1, 5, endpoint = True))

plt.plot(X, C)
plt.plot(X, S)

plt.show()
