import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f2():
    data1 = pd.read_csv("task_1/train/train_meta.csv")
    data2 = pd.read_csv("task_1/train/train_gts.csv")
    pd.set_option('display.max_columns', None)
    # print(data1)
    # print(list(data1.columns.values))
    for i in range(1, 10):
        print(data1.loc[[i]])
    # for i in range(1, 100):
    #     print(data2.loc[[i]])


def f1():
    with open("task_1/train/00617_hr.npy", "rb") as f:
        data3 = np.load(f, allow_pickle=True)
    with open("task_1/train/00034_hr.npy", "rb") as f:
        data4 = np.load(f, allow_pickle=True)

    for i in range(len(data3)):
        plt.plot(data4[i], color='r')
        plt.plot(data3[i], color='b')
        plt.show()


# f2()
f1()
