import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f2():
    data1 = pd.read_csv("train/train_meta.csv")
    sr = set()
    for data in data1["infarction_stadium1"]:
        sr.add(data)
    print(sr)


def f1():
    with open("train/00034_hr.npy", "rb") as f:
        data3 = np.load(f, allow_pickle=True)
    with open("train/00034_hr.npy", "rb") as f:
        data4 = np.load(f, allow_pickle=True)

    for i in range(len(data3)):
        plt.plot(data4[i], color='r')
        plt.plot(data3[i], color='b')
        plt.show()


f2()
# f1()
