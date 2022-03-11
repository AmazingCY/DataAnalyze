# -*- coding: utf-8 -*-
# @Time : 2022/2/22 9:49
# @Author : Cao yu
# @File : draw.py
# @Software: PyCharm

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def draw4_3():
    # 实验数据
    pre1 = [0.2295, 0.2305, 0.2291]
    # pre1 = [i*100 for i in pre1]
    pre5 = [0.1444, 0.1442, 0.1437]
    # pre5 = [i*100 for i in pre5]
    pre10 = [0.0781, 0.0776, 0.0774]
    # pre10 = [i*100 for i in pre10]
    map = [0.5747, 0.5752, 0.5727]

    x = np.arange(3)
    bar_width = 0.2
    tick_label = ["30", "40", "50"]
    plt.xlabel('序列长度')  # x轴标题
    plt.ylabel('预测精确度')  # y轴标题
    plt.title('AIS_LONG5K数据集实验结果')
    # plt.plot(num, map, marker='o', markersize=4, c='b', label='MAP')  # 绘制折线图，添加数据点，设置点的大小
    plt.bar(x - bar_width, pre1, bar_width, color="r", align="center", label="Precision@1", alpha=0.5)
    plt.bar(x, pre5, bar_width, color="g", align="center", label="Precision@5", alpha=0.5)
    plt.bar(x + bar_width, pre10, bar_width, color="b", align="center", label="Precision@10", alpha=0.5)

    my_y_ticks = np.arange(0, 0.3, 0.01)
    plt.xticks(x - bar_width / 24, tick_label)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper right')
    plt.savefig('4-3.tif')
    plt.show()


def draw4_4():
    window = [3, 6, 9, 12, 15]
    long5k = [0.5727, 0.5635, 0.5643, 0.5667, 0.5671]
    long4k = [0.5819, 0.5734, 0.5751, 0.5742, 0.5758]
    long3k = [0.5899, 0.5784, 0.5816, 0.5861, 0.5876]
    plt.xlabel('窗口大小')  # x轴标题
    plt.ylabel('平均精度均值')  # y轴标题
    plt.title('不同窗口大小实验结果')
    plt.plot(window, long5k, marker='o', markersize=4, c='g', linestyle='dashed', label='AIS_LONG5K@50')
    plt.plot(window, long4k, marker='o', markersize=4, c='r', linestyle='dotted', label='AIS_LONG4K@40')
    plt.plot(window, long3k, marker='o', markersize=4, c='b', linestyle='dashdot', label='AIS_LONG3K@30')
    my_x_ticks = np.arange(3, 18, 3)
    my_y_ticks = np.arange(0.55, 0.62, 0.01)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper right')
    plt.savefig('4-4.tif')
    plt.show()


def draw4_5():
    # 实验数据
    norm = [0.5899, 0.5819, 0.5727]
    un_norm = [0.2757, 0.2678, 0.2467]

    x = np.arange(3)
    bar_width = 0.3
    tick_label = ["AIS_LONG3K@30", "AIS_LONG4K@40", "AIS_LONG5K@50"]
    plt.xlabel('AIS数据集')  # x轴标题
    plt.ylabel('平均精度均值')  # y轴标题
    plt.title('层归一化对比实验')
    # plt.plot(num, map, marker='o', markersize=4, c='b', label='MAP')  # 绘制折线图，添加数据点，设置点的大小
    plt.bar(x - bar_width / 2, norm, bar_width, color="r", align="center", label="LayerNorm", alpha=0.5)
    plt.bar(x + bar_width / 2, un_norm, bar_width, color="b", align="center", label="unLayerNorm", alpha=0.5)

    my_y_ticks = np.arange(0, 0.8, 0.05)
    plt.xticks(x - bar_width / 24, tick_label)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper right')
    plt.savefig('4-5.tif')
    plt.show()


def draw4_6():
    length = [30, 40, 50]
    RNN = [1074.4, 2269.6, 3189.3]
    RNN = [i / 60 for i in RNN]
    LSTM = [7993, 8083.2, 8231.7]
    LSTM = [i / 60 for i in LSTM]
    GRU = [8027.8, 8163.9, 8312.4]
    GRU = [i / 60 for i in GRU]
    Transformer = [127, 135.6, 141.8]
    STW_RNN = [131.2, 140.7, 150.1]
    plt.xlabel('序列长度')  # x轴标题
    plt.ylabel('训练时间/min')  # y轴标题
    plt.title('RNN类模型训练时间对比')
    plt.plot(length, RNN, marker='o', markersize=4, c='g', linestyle='dashed', label='RNN')
    plt.plot(length, LSTM, marker='o', markersize=4, c='r', linestyle='dotted', label='LSTM')
    plt.plot(length, GRU, marker='o', markersize=4, c='b', linestyle='dashdot', label='GRU')
    my_x_ticks = np.arange(30, 55, 5)
    my_y_ticks = np.arange(10, 180, 10)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper right')
    plt.savefig('4-6.tif')
    plt.show()


def draw4_7():
    length = [30, 40, 50]
    Transformer = [127, 135.6, 141.8]
    STW_RNN = [131.2, 140.7, 150.1]
    plt.xlabel('序列长度')  # x轴标题
    plt.ylabel('训练时间/s')  # y轴标题
    plt.title('模型训练时间对比')
    plt.plot(length, Transformer, marker='o', markersize=4, c='g', linestyle='dashed', label='Transformer')
    plt.plot(length, STW_RNN, marker='o', markersize=4, c='r', linestyle='dotted', label='STW_RNN')
    my_x_ticks = np.arange(30, 55, 5)
    my_y_ticks = np.arange(125, 160, 5)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper right')
    plt.savefig('4-7.tif')
    plt.show()


def draw4_8():
    # 实验数据
    Transformer_time = [0.4919, 0.4908, 0.4858]
    STW_RNN_time = [0.5081, 0.5092, 0.5142]

    Transformer_pre = [0.2117, 0.2090, 0.2052]
    STW_RNN_pre = [0.2375, 0.2333, 0.2291]

    trans_eff = [0.4304, 0.4258, 0.4224]
    STW_RNN_eff = [0.4674, 0.4581, 0.4455]

    x = np.arange(3)
    bar_width = 0.3
    tick_label = ["AIS_LONG3K@30", "AIS_LONG4K@40", "AIS_LONG5K@50"]
    plt.xlabel('AIS数据集')  # x轴标题
    plt.ylabel('综合预测效率')  # y轴标题
    plt.title('预测效率对比实验')
    # plt.plot(num, map, marker='o', markersize=4, c='b', label='MAP')  # 绘制折线图，添加数据点，设置点的大小
    plt.bar(x - bar_width / 2, trans_eff, bar_width, color="r", align="center", label="Transformer", alpha=0.5)
    plt.bar(x + bar_width / 2, STW_RNN_eff, bar_width, color="b", align="center", label="STW-RNN", alpha=0.5)

    my_y_ticks = np.arange(0, 0.6, 0.05)
    plt.xticks(x - bar_width / 24, tick_label)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper right')
    plt.savefig('4-8.tif')
    plt.show()


def draw5_4():
    length = [16, 32, 64, 128]
    GRU = [0.6176, 0.6422, 0.6583, 0.6598]
    BiGRU = [0.6138, 0.6479, 0.6596, 0.6634]
    Falsh = [0.6048, 0.6408, 0.6647, 0.6621]
    AT_GRU = [0.6398, 0.6878, 0.7157, 0.7218]
    SEAT_GRU = [0.6324, 0.6897, 0.7249, 0.7318]

    plt.xlabel('词嵌入维度大小')  # x轴标题
    plt.ylabel('平均精度均值')  # y轴标题
    plt.title('AIS_SPARSE词嵌入维度对比')

    plt.plot(length, GRU, marker='o', markersize=4, c='g', linestyle='dashed', label='GRU ')
    plt.plot(length, BiGRU, marker='o', markersize=4, c='r', linestyle='dotted', label='BiGRU')
    plt.plot(length, Falsh, marker='o', markersize=4, c='b', linestyle='dashdot', label='Flashback')
    plt.plot(length, AT_GRU, marker='o', markersize=4, c='y', linestyle='dashed', label='AT-BiGRU')
    plt.plot(length, SEAT_GRU, marker='o', markersize=4, c='c', linestyle='dashdot', label='SEAT-GRU')

    my_x_ticks = np.arange(16, 144, 16)
    my_y_ticks = np.arange(0.6, 0.8, 0.01)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper right')
    plt.savefig('5-4.tif')
    plt.show()


def draw5_5():
    x = np.arange(4)
    y1 = [0.2198,
          0.2515,
          0.2662,
          0.2665
          ]
    y2 = [0.6065,
          0.6703,
          0.6879,
          0.6769
          ]

    y3 = [0.3883,
          0.4505,
          0.4719,
          0.4691
          ]

    bar_width = 0.3
    tick_label = ["7", "13", "25", "31"]

    # 生成多数据并列柱状图
    plt.bar(x - bar_width, y1, bar_width, color="c", align="center", label="Gowalla", alpha=0.5)
    plt.bar(x, y2, bar_width, color="g", align="center", label="Brightkite", alpha=0.5)
    plt.bar(x + bar_width, y3, bar_width, color="b", align="center", label="Foursquare", alpha=0.5)
    # 生成多数据平行柱状图
    # plt.barh(x,y,bar_width,color="c",align="center",label="班级A",alpha=0.5)
    # plt.barh(x+bar_width,y1,bar_width,color="b",align="center",label="班级B",alpha=0.5)

    # 设置x,y轴标签
    plt.xlabel("词嵌入维度大小")
    plt.ylabel("平均精度均值")
    my_y_ticks = np.arange(0, 0.9, 0.1)

    # 设置x轴标签位置
    plt.title('社交签到数据集词嵌入维度对比')
    plt.xticks(x - bar_width / 24, tick_label)
    plt.yticks(my_y_ticks)
    plt.legend(loc='upper left')
    plt.savefig('dim.tif', bbox_inches='tight')
    plt.show()


def draw5_7():
    length_gowalla = [10, 20, 30]
    gow_map = [0.2515, 0.3294, 0.3749]
    gow_recall5 = [0.3617, 0.4627, 0.5138]
    gow_recall1 = [0.1549, 0.2160, 0.2574]
    gow_f1 = [0.0964, 0.1472, 0.1775]
    gow_f5 = [0.1009, 0.1958, 0.2487]

    length_ais = [5, 10, 15, 20]
    recall_1 = [0.5524, 0.6002, 0.6273, 0.6469]
    f_1 = [0.3585, 0.3972, 0.4152, 0.4238]
    recall_5 = [0.7318, 0.8074, 0.8247, 0.8371]
    f_5 = [0.2436, 0.2658, 0.2724, 0.2749]
    map = [0.6245, 0.6897, 0.7063, 0.7198]

    plt.subplot(121)
    plt.title('Gowalla')
    plt.xlabel('各位置标识总数')  # x轴标题
    plt.ylabel('预测值')  # y轴标题
    plt.plot(length_gowalla, gow_map, marker='o', markersize=4, c='b', linestyle='dashed')  # 绘制折线图，添加数据点，设置点的大小
    plt.plot(length_gowalla, gow_recall1, marker='o', markersize=4, c='g', linestyle='dotted')
    plt.plot(length_gowalla, gow_f1, marker='o', markersize=4, c='y', linestyle='dashdot')
    plt.plot(length_gowalla, gow_recall5, marker='o', markersize=4, c='c', linestyle='dotted')
    plt.plot(length_gowalla, gow_f5, marker='o', markersize=4, c='r', linestyle='dashdot')

    my_x_ticks = np.arange(10, 35, 5)
    plt.xticks(my_x_ticks)
    my_y_ticks = np.arange(0.05, 0.6, 0.05)
    plt.yticks(my_y_ticks)

    plt.subplot(122)
    plt.title('AIS_SPARSE')
    plt.xlabel('各位置标识总数')  # x轴标题
    plt.ylabel('预测值')  # y轴标题
    plt.plot(length_ais, map, marker='o', markersize=4, c='b', linestyle='dashed')
    plt.plot(length_ais, recall_1, marker='o', markersize=4, c='g', linestyle='dotted')
    plt.plot(length_ais, f_1, marker='o', markersize=4, c='y', linestyle='dashdot')
    plt.plot(length_ais, recall_5, marker='o', markersize=4, c='c', linestyle='dotted')
    plt.plot(length_ais, f_5, marker='o', markersize=4, c='r', linestyle='dashdot')

    my_x_ticks = np.arange(5, 25, 5)
    plt.xticks(my_x_ticks)
    my_y_ticks = np.arange(0.2, 0.9, 0.05)
    plt.yticks(my_y_ticks)

    leg = plt.legend(['MAP', 'Recall@1', 'F-score@1', 'Recall@5', 'F-score@5'], loc='upper left', bbox_to_anchor=(1, 1),
                     fontsize=9)
    plt.tight_layout()
    plt.savefig('5-7.tif', bbox_inches='tight')
    plt.show()  # 显示折线图


if __name__ == "__main__":
    draw5_7()

