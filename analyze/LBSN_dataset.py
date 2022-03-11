# -*- coding: utf-8 -*-
# @Time : 2021/11/9 22:05
# @Author : Cao yu
# @File : LBSN_dataset.py
# @Software: PyCharm

from datetime import datetime
import time
from DataAnalyze import *

time_baseline = datetime(2009, 1, 1)

gowalla_data = {}
find_user = {}
total_records = 0
average_per_user_records = 0


if __name__ == "__main__":

    file_path = "data//AIS_dataset.txt"
    analyze_data = DataAnalyze(file_path).data_loader_txt()
    total_records = len(analyze_data)
    print(f"This dataset has {total_records} records.")

    for line in analyze_data:
        content = line.strip().split('\t')
        user_id = int(float(content[0]))
        #trans_time = time.mktime((datetime.strptime(content[1], "%Y-%m-%dT%H:%M:%SZ")).timetuple())
        #user_time = trans_time - time.mktime(time_baseline.timetuple())
        user_time = content[1]
        user_latitude = float(content[2])
        user_longitude = float(content[3])
        user_coordinate = (user_latitude, user_longitude)
        user_location = int(content[4])

        if user_id not in gowalla_data:
            gowalla_data[user_id] = [[user_time,user_coordinate,user_location]]
        else:
            gowalla_data[user_id].append([user_time,user_coordinate,user_location])

    average_per_user_records = total_records//len(gowalla_data)
    print(f"Average records of users:{average_per_user_records}.")

    for record in gowalla_data[303104000]:
        if record[-1] not in find_user:
            find_user[record[-1]] = [record[:-1]]
        else:
            find_user[record[-1]].append(record[:-1])

    for key,value in find_user.items():
        if len(value)>1:
            print(f"loc:{key}")
            print(f"record:{value}")










