import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk


def f2():
    data1 = pd.read_csv("task_1/train/train_meta.csv")
    data2 = pd.read_csv("task_1/train/train_gts.csv")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    # print(data1)
    # print(list(data1.columns.values))
    # for i in range(1, 10):
    #     print(data1.loc[[i]])
    # for i in range(1, 100):
    #     print(data2.loc[[i]])
    name = list(data1['record_name'])
    meta = [-1] * len(name)
    for i in range(len(name)):
        df = data2.loc[data2['record_name'] == name[i]]
        meta[i] = df['myocard'].loc[df.index[0]]
    data1['myocard'] = meta
    print(data1[['strat_fold', 'record_name', 'myocard']])
    e = set(data1['infarction_stadium1']) | set(data1['infarction_stadium2'])
    print(e)
    # print(data1['record_name'])


def f1():
    with open("task_1/train/00483_hr.npy", "rb") as f:
        data3 = np.load(f, allow_pickle=True)
    with open("task_1/train/01223_hr.npy", "rb") as f:
        data4 = np.load(f, allow_pickle=True)

    for i in range(len(data3)):
        plt.plot(data4[i], color='r')
        plt.plot(data3[i], color='b')
        plt.show()


def f3():
    with open("task_1/train/00483_hr.npy", "rb") as f:
        data3 = np.load(f, allow_pickle=True)
    with open("task_1/train/01223_hr.npy", "rb") as f:
        data4 = np.load(f, allow_pickle=True)
    signals, info = nk.ecg_process(data3[0], sampling_rate=512)
    # df = nk.ecg_analyze(signals, sampling_rate=512)
    # print(df)
    nk.ecg_plot(signals, info)
    fig = plt.gcf()
    fig.set_size_inches(10, 12, forward=True)
    fig.savefig('myfig.png')


# f2()
# f1()
f3()
