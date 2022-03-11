# -*- coding: utf-8 -*-
# @Time : 2022/1/12 21:08
# @Author : Cao yu
# @File : interpolation.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# Program 0.5 Hermite Interpolation

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 数据准备
X = np.array([
              36.86005,36.86190,36.86365,36.86517,\
              36.86714,36.86899,36.8707,36.87303,36.87584,\
             36.87859,36.88125,36.88388,36.88655,36.8877,36.8904,\
             36.89313,36.89574,36.89852,36.90124,36.90913])  # 定义样本点X，从-pi到pi每次间隔1
Y = np.array([
              -76.31622,-76.31867,-76.32109,-76.32318,\
              -76.32594,-76.32851,-76.33046,-76.33218,-76.33339,\
              -76.33386,-76.33408,-76.33433,-76.3347,-76.33485,-76.33521,\
              -76.3356,-76.33606,-76.33652,-76.33698,-76.33814])  # 定义样本点Y，形成sin函数

Z_x = np.array([36.86788,36.90412,36.907412])
Z_y = np.array([-76.32695,-76.33741,-76.33798])

c_x = np.array([36.86802,36.86756])
c_y = np.array([-76.32626,-76.32766])

new_x = np.arange(36.86, 36.912, 0.0025)  # 定义差值点

# 进行样条差值
import scipy.interpolate as spi

# 进行一阶样条插值
ipo1 = spi.splrep(X, Y, k=1)  # 样本点导入，生成参数
iy1 = spi.splev(new_x, ipo1)  # 根据观测点和样条参数，生成插值

# 进行三次样条拟合
ipo3 = spi.splrep(X, Y, k=3)  # 样本点导入，生成参数
iy3 = spi.splev(new_x, ipo3)  # 根据观测点和样条参数，生成插值

##作图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 8))
matplotlib.rcParams.update({'font.size': 13})

ax1.plot(X, Y, 'o', label='位置点',markersize=6)

ax1.scatter(Z_x,Z_y,marker='o',c='',edgecolors='r',s=250)
ax1.text(Z_x[0], Z_y[0], ('存在缺失值'),ha='left', va='bottom', fontsize=13)
#ax1.plot(new_x, iy1, label='插值点')
ax1.set_ylim(Y.min() - 0.001, Y.max() + 0.001)
ax1.set_xlabel('纬度',fontsize=13)
ax1.set_ylabel('经度',fontsize=13)
ax1.set_title('原始位置序列图')
ax1.tick_params(labelsize=13)
ax1.legend()



ax2.plot(X, Y, 'o', label='位置点',markersize=6)
ax2.plot(Z_x,Z_y,'*',label='最终插入值',c='r',markersize=12)
ax2.plot(c_x,c_y,'^',label='运动线性插值点',c='g',markersize=10)
ax2.plot(c_x,c_y,c='r',linestyle='dashed')
plt.text(c_x[0], c_y[0], (c_x[0],c_y[0]),ha='left', va='bottom', fontsize=10)
plt.text(Z_x[0], Z_y[0], (Z_x[0],Z_y[0]),ha='left', va='bottom', fontsize=10)
plt.text(c_x[1], c_y[1], (c_x[1],c_y[1]),ha='right', va='top', fontsize=10)

ax2.plot(new_x, iy3, label='三次样条插值曲线',c='c',markersize=5)
ax2.set_ylim(Y.min() - 0.001, Y.max() + 0.001)
ax2.set_xlabel('纬度',fontsize=13)
ax2.set_ylabel('经度',fontsize=13)
ax2.set_title('缺失值补充示意图')
ax2.tick_params(labelsize=13)
ax2.legend()

#plt.savefig('interpolation.tif')
plt.show()

