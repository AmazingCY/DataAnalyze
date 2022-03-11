# -*- coding: utf-8 -*-
# @Time : 2022/1/6 16:57
# @Author : Cao yu
# @File : data_processing.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random


def analyze(data, name):
    print(f"Now analyze {name}!")
    record_collect = {}
    record_location = {}
    collect_location = set()
    record_count = 0
    time_count_each = 0
    time_count_total = 0
    pre_record = data[0].split('\t')[0]
    pre_time = float(data[0].split('\t')[1])
    for line in data:
        record = line.strip().split('\t')
        collect_location.add(record[-1])
        if record[0] == pre_record:
            record_count += 1
            time_count_each += (pre_time - float(record[1]))
            pre_time = float(record[1])
            if record[-1] not in record_location:
                record_location[record[-1]] = 1
            else:
                record_location[record[-1]] += 1
        else:
            if pre_record not in record:
                record_collect[pre_record] = (record_count, record_location)

            time_count_total += (time_count_each // (record_count - 1))
            record_count = 0
            record_location = {}
            pre_record = record[0]
            pre_time = float(record[1])

    demo = record_collect[list(record_collect.keys())[0]]
    print(f"The length of {name} is {len(data)}.")
    print(f"The number of object is {len(record_collect)}.")
    print(f"The number of location is {len(collect_location)}.")
    print(f"The average record of each object is {len(data) // len(record_collect)}.")
    print(f"The average time interval of each object is {time_count_total // len(record_collect)}.")
    print(f"The record of demo is {demo}")


def select_column(data, path):
    file = open(path, 'w')
    for line in data:
        record = line.strip().split('\t')
        new_record = record[:4] + [record[-1]]
        new_line = '\t'.join(new_record) + '\n'
        file.write(new_line)
    file.close()
    print("Have selected column successfully !")


def cut_dataset(cut_file, save_file, cut_range: list):
    data = pd.read_csv(cut_file, header=0, sep=',', low_memory=False)
    record = len(data)
    record_sign = 0
    ship_id = 0
    while record_sign < record:
        start = record_sign
        end = start + random.randint(cut_range[0], cut_range[-1])
        if end < record:
            data.loc[start:end, "MMSI"] = ship_id
        else:
            data.loc[start:, "MMSI"] = ship_id
        record_sign = end + 1
        ship_id += 1
    data.to_csv(save_file, index=False, sep=',')
    print(f"Cut from {cut_range[0]} to {cut_range[-1]}")


def filter_location(filter_file, save_file, num):
    data = pd.read_csv(filter_file, header=0, sep=',', low_memory=False)
    # for filter locations
    data["count_id"] = data.groupby("id", group_keys=False)["id"].transform("count")
    data = data.drop(data[data.count_id < num].index)
    # for filter Users
    data["count_ship"] = data.groupby("MMSI", group_keys=False)["MMSI"].transform("count")
    data = data.drop(data[data.count_ship < 300].index)

    data = data.drop(['count_id', 'count_ship'], axis=1)
    data.to_csv(save_file, index=False, sep=',')

    user_id = data['MMSI'].unique()
    poi_id = data['id'].unique()
    print(f"Filter {num} locations")
    print("After filter,total have %d Ships " % len(user_id))
    print("After filter,total have %d Locations " % len(poi_id))
    print("END!")


def draw_dataset(data):
    lat = []
    lon = []
    for line in data:
        record = line.strip().split('\t')
        lat.append(float(record[2]))
        lon.append(float(record[3]))

    plt.xlabel("LON")
    plt.ylabel("LAT")
    for index in range(len(lat)):
        plt.plot(lon[index], lat[index], marker='o', markersize=5, c='b')
    my_x_ticks = np.arange(36.8385, 36.8386, 0.0001)
    plt.xticks(my_x_ticks)
    # my_y_ticks = np.arange(0.15, 0.65, 0.05)
    # plt.yticks(my_y_ticks)
    plt.show()


def split_dataset(data, path):
    file = open(path, 'w')
    for line in data:
        record = line.strip().split('\t')
        new_record = record[:4] + [record[-1]]
        new_line = '\t'.join(new_record) + '\n'
        file.write(new_line)
    file.close()
    print("Have selected column successfully !")


def txt2csv(txt_file, csv_file):
    ship_num_tmp = []
    time_tmp = []
    lat_tmp = []
    longit_tmp = []
    SOG_tmp = []
    COG_tmp = []
    location_id = []

    data = open(txt_file, 'r')
    lines = data.readlines()
    for line in lines:
        line = line.strip().split('\t')
        try:
            ship_num_tmp.append(int(line[0]))
            # transtime = time.mktime((datetime.strptime(line[1], "%Y-%m-%dT%H:%M:%S")).timetuple())
            time_tmp.append(float(line[1]))
            lat_tmp.append(float(line[2]))
            longit_tmp.append(float(line[3]))
            SOG_tmp.append(float(line[4]))
            COG_tmp.append(float(line[5]))
            location_id.append(line[6])
        except:
            print(line)

    dataframe = pd.DataFrame(
        {'MMSI': ship_num_tmp, 'time': time_tmp, 'latitude': lat_tmp, 'longitude': longit_tmp, 'SOG': SOG_tmp,
         "COG": COG_tmp, "id": location_id})
    User_ID = list(set(dataframe.MMSI.values))
    for index in range(len(User_ID)):
        tmp = dataframe.loc[dataframe.MMSI == User_ID[index]]
        tmp = tmp.copy()
        tmp.sort_values("time", ascending=False, inplace=True)
        if index == 0:
            tmp.to_csv(csv_file, index=False, sep=',', mode="a")
        else:
            tmp.to_csv(csv_file, index=False, sep=',', mode="a", header=0)
    print("trans successfully!")


def csv2txt(file_name):
    data = pd.read_csv(file_name + ".csv", header=0, sep=',', low_memory=False)
    data.to_csv(file_name + ".txt", index=False, sep='\t',header=0)


if __name__ == "__main__":
    file_list = ["AIS/AIS_one_month_long.txt","AIS/AIS_filter_sparse_10.txt","AIS/AIS_filter.txt"]
    file_save_list = ["AIS/AIS_one_month_short_GRU.txt", "AIS/AIS_one_month_short_split.txt"]
    file_draw_list = ["AIS/AIS_demo.txt"]
    file_trans_list = ["AIS/AIS_filter.csv", "AIS/AIS_filter_5.csv", "AIS/AIS_filter_10.csv", "AIS/AIS_filter_15.csv"]
    file_cut_list = ["AIS/AIS_filter_sparse.csv","AIS/AIS_filter_long3000.csv","AIS/AIS_filter_long4000.csv",\
                     "AIS/AIS_filter_long5000.csv"]
    file_filter_list = ["AIS/AIS_filter_sparse_5.csv", "AIS/AIS_filter_sparse_10.csv", "AIS/AIS_filter_sparse_15.csv",\
                        "AIS/AIS_filter_long_3K.csv", "AIS/AIS_filter_long_4K.csv", "AIS/AIS_filter_long_5K.csv"]

    print("A script to process AIS data")
    print("Support operation |analyze|select|draw|split|txt2csv|csv2txt|filter|cut|")
    flag = input("Please choose operation: ")

    if flag == 'analyze':
        for file_index in file_list:
            process_file = open("data/" + file_index, "r")
            print("#" * 50)
            analyze(process_file.readlines(), file_index)

    elif flag == 'select':
        select_file = open("data/" + file_list[2], "r")
        select_column(select_file, "data/" + file_save_list[0])

    elif flag == 'draw':
        process_file = open("data/" + file_draw_list[0], "r")
        draw_dataset(process_file)

    elif flag == 'split':
        split_file = open("data/" + file_list[2], "r")
        split_dataset(split_file, "data/" + file_save_list[1])

    elif flag == 'txt2csv':
        txt_file = "data/" + file_list[-1]
        csv_file = "data/" + file_trans_list[0]
        txt2csv(txt_file, csv_file)

    elif flag == 'csv2txt':
        for file in file_filter_list[3:]:
            csv2txt("data/" + file[:-4])

    elif flag == 'filter':
        filter_num = [5]
        for index in range(len(filter_num)):
            filter_file = "data/" + file_cut_list[1]
            save_file = "data/" + file_filter_list[3]
            filter_location(filter_file, save_file, filter_num[index])

    elif flag == 'cut':
        cut_file = "data/" + file_trans_list[0]
        save_file = "data/" + file_cut_list[3]
        cut_dataset(cut_file, save_file, [4800,5200])
