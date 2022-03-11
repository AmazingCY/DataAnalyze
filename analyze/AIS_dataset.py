# -*- coding: utf-8 -*-
# @Time : 2021/11/10 16:13
# @Author : Cao yu
# @File : AIS_filter.py
# @Software: PyCharm

import pandas as pd
import random
from DataAnalyze import *
from tqdm import tqdm

AIS_data = {}
total_records = 0
average_per_user_records = 0
location_label = {}
label = []


def data_select(csv_file, index):
    user_record = None
    user_record_tmp = None
    analyze_data = DataAnalyze([], csv_file).data_filter()
    # total_records = len(analyze_data.index)

    # print(f"This dataset has {total_records} records.")
    useful_column = ['MMSI', 'BaseDateTime', 'LAT', 'LON', 'SOG', 'COG']
    useful_analyze_data = analyze_data[useful_column]

    user_id = set(useful_analyze_data.iloc[:, 0].values)
    # average_per_user_records = total_records//len(user_id)
    # print(f"Average records of users:{average_per_user_records}.")

    for id in user_id:

        if user_record is None:
            user_record = useful_analyze_data.query('MMSI == ' + str(id))
        else:
            user_record_tmp = useful_analyze_data.query('MMSI == ' + str(id))
            user_record = user_record.append(user_record_tmp)

    # save_txt
    # user_record.to_csv("data//AIS_test.txt", sep='\t', index=False)
    # save_csv
    user_record.to_csv("D:/DataAnalyze/AIS/AIS_15000.csv", sep=',', index=False)

    # print("*******************************")
    # print("have select 2000:" + str(index))
    # return user_record


def data_merge_one(num):
    data = pd.DataFrame()
    for index in range(5, num):
        file_path_csv = "./AIS_three_" + str(index + 1) + "_2000.csv"
        data_tmp = DataAnalyze(file_path_csv).data_loader_csv()
        # one_record = data_tmp.query('MMSI==367396710')
        data = pd.concat([data, data_tmp], ignore_index=True)
    data.to_csv("./data/AIS_half_month_2.csv", sep=',', index=False)

    # print("*******************************")
    # print("have merge AIS_three_: " + str(num + 1))

def pri_select(num):
    for index in range(num):
        file_path_csv = "./data/AIS_half_month_1.csv"
        data = data_select(file_path_csv, num)
        data.to_csv("AIS_filter_1.csv", sep=',', index=False)

        print("*******************************")
        print("have deal:{}".format(index + 1))


def time_sort(dataset):
    data = dataset
    User_ID = list(set(data.MMSI.values))
    for index in range(len(User_ID)):
        tmp = data.loc[data.MMSI == User_ID[index]]
        tmp = tmp.copy()
        tmp.sort_values("time", ascending=False, inplace=True)
        if index == 0:
            tmp.to_csv("AIS_sort_15000.csv", index=False, sep=',', mode="a")
        else:
            tmp.to_csv("AIS_sort_15000.csv", index=False, sep=',', mode="a", header=0)

def location_mark(file):

    file_path_txt = file
    analyze_data = DataAnalyze(file_path_txt).data_loader_txt()
    total_records = len(analyze_data)
    print(f"This dataset has {total_records} records.")
    f = open("../data/AIS_dataset.txt", mode="r+")

    for line in tqdm(analyze_data,desc="Location Mark"):

        content = line.strip().split('\t')
        user_id = int(float(content[0]))
        # trans_time = time.mktime((datetime.strptime(content[1], "%Y-%m-%dT%H:%M:%SZ")).timetuple())
        # user_time = trans_time - time.mktime(time_baseline.timetuple())
        user_time = content[1]
        user_latitude = float(content[2])
        user_longitude = float(content[3])
        user_coordinate = (user_latitude, user_longitude)

        if user_coordinate not in location_label:
            new_label = random.randint(1, 10 ** 7)
            while new_label in label:
                new_label = random.randint(1, 10 ** 7)
            label.append(new_label)
            location_label[user_coordinate] = new_label
            user_location = new_label
        else:
            user_location = location_label[user_coordinate]

        content.append(str(user_location))

        f.write("\t".join(content)+"\n")

    f.close()


if __name__ == "__main__":

    file_path = "AIS_sort_15000.csv"
    location_mark(file_path)
    pass


