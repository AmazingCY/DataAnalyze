# -*- coding: utf-8 -*-
# @Time : 2021/11/8 17:13
# @Author : Cao yu
# @File : DataAnalyze.py
# @Software: PyCharm

import pandas as pd
import numpy as np


class DataAnalyze(object):
    __slots__ = ["__input_data", "__file_path"]

    def __init__(self, input_data=None, file_path=None):
        self.__input_data = input_data
        self.__file_path = file_path

    def data_loader_txt(self):
        file = open(self.__input_data, mode='r')
        file_lines = file.readlines()
        return file_lines

    def data_loader_csv(self):
        df = pd.read_csv(self.__input_data, sep=',', low_memory=False)
        return df

    def data_filter(self):
        data = pd.read_csv(self.__file_path, header=0, sep=',', low_memory=False)
        # data["count_poi"] = data.groupby("POI_ID", group_keys=False)["POI_ID"].transform("count")
        # data = data.drop(data[data.count_poi < 10].index)
        # for filter Users
        data["count_user"] = data.groupby("MMSI", group_keys=False)["MMSI"].transform("count")
        data = data.drop(data[data.count_user >15000].index)
        data = data.drop(data[data.SOG==0].index)
        data = data.drop(['count_user'], axis=1)
        return data



