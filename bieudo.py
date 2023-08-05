# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:13:01 2023

@author: Khiem
"""

import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("C:/Users/Khiem/Desktop/big_data/data/ketqua_win.csv")
data_2 = pd.read_csv("C:/Users/Khiem/Desktop/big_data/data/ketqua_ubuntu.csv")
data_3 = pd.read_csv("C:/Users/Khiem/Desktop/big_data/data/ketqua_win_accuracy.csv")
data_4 = pd.read_csv("C:/Users/Khiem/Desktop/big_data/data/ketqua_ubuntu_accuracy.csv")




data.head()
plt.figure(figsize=(15,9))
plt.plot(data.Ten_file, data.Chay_thuong, label ="thời gian chạy thương" )
plt.plot(data.Ten_file, data.Spark, label ="thời gian chạy bằng spark" )
plt.plot(data_2.Ten_file, data_2.Cluster, label ="thời gian chạy bằng cluster" )

plt.title("So sánh tốc độ chạy thường và chạy bằng spark", fontsize = 23)
plt.xlabel("Tên file", fontsize = 16)
plt.ylabel("Thời gian chạy", fontsize = 16)
plt.legend(loc = "best", fontsize = 16)
plt.grid()
plt.show()





data_2.head()
plt.figure(figsize=(15,9))
plt.plot(data_2.Ten_file, data_2.Spark, label ="thời gian chạy spark" )
plt.plot(data_2.Ten_file, data_2.Cluster, label ="thời gian chạy bằng cluster" )

plt.title("So sánh tốc độ chạy spark và chạy cluster", fontsize = 23)
plt.xlabel("Tên file", fontsize = 16)
plt.ylabel("Thời gian chạy", fontsize = 16)
plt.legend(loc = "best", fontsize = 16)
plt.grid()
plt.show()






plt.figure(figsize=(15,9))
plt.plot(data_3.Ten_file, data_3.Chay_thuong, label ="accuracy khi chạy thường" )
plt.plot(data_3.Ten_file, data_3.Spark, label ="accuracy khi chạy spark" )
plt.ylim(0, 1)
plt.title("So sánh accuracy khi chạy thường và chạy spark", fontsize = 23)
plt.xlabel("Tên file", fontsize = 16)
plt.ylabel("Accuracy", fontsize = 16)
plt.legend(loc = "best", fontsize = 16)
plt.grid()
plt.show()






plt.figure(figsize=(15,9))
plt.plot(data_4.Ten_file, data_4.Spark, label ="accuracy khi chạy bằng spark" )
plt.plot(data_4.Ten_file, data_4.Cluster, label ="accuracy khi chạy bằng spark cluster" )
plt.ylim(0, 1)
plt.title("So sánh accuracy khi chạy spark và khi chạy spark cluster", fontsize = 23)
plt.xlabel("Tên file", fontsize = 16)
plt.ylabel("Accuracy", fontsize = 16)
plt.legend(loc = "best", fontsize = 16)
plt.grid()
plt.show()