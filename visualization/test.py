# -*- coding: utf-8 -*-
# @Time : 2021/11/19 22:05
# @Author : Cao yu
# @File : test.py
# @Software: PyCharm



from pyecharts.faker import Collector
from pyecharts.charts import Page, Bar, Line
from pyecharts import options as opts
C = Collector() #收集需要建立的图表
@C.funcs
def bar()->Bar:
    c = (
        Bar()
        .add_xaxis(["92.6", "227", "333.33", "446.4", "530","535", "630","641", "757.6","833.33","926"])
        .add_yaxis("1#", [101, 227, 325, 428,510, 520, 580,622, 734, 805, 895], )
        .add_yaxis("2#", [67, 204, 312, 421, 513,526, 580,632, 749, 828, 919], )
        .add_yaxis("3#", [73, 207, 311, 419,512, 519, 581,621, 739, 811, 910], )
        .add_yaxis("4#", [100, 228, 326, 433,511, 530, 582,628, 739, 814, 905], )
        .add_yaxis("5#", [81, 216, 319, 428, 512,527, 581,635, 746, 823, 921], )
        .set_global_opts(title_opts=opts.TitleOpts(title="OCP 测试数据"),
        	yaxis_opts=opts.AxisOpts(name="测试值(mA)"),
            xaxis_opts=opts.AxisOpts(name="设置值(mA)"),)
    )
    return c

