import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk
import time


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
    k = 5
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    with open("task_1/train/21682_hr.npy", "rb") as f:
        data3 = np.load(f, allow_pickle=True)
    with open("task_1/train/01223_hr.npy", "rb") as f:
        data4 = np.load(f, allow_pickle=True)
    q = nk.ecg_clean(data3[k], sampling_rate=500)
    signals, info = nk.ecg_delineate(q, sampling_rate=500)
    plt.plot(q)
    # plt.plot(data3[k])
    # print(signals)
    # print(info)
    for i in info:
        print(i, info[i])
    for i in info['ECG_R_Offsets']:
        if not (isinstance(i, float)):
            plt.plot([i, i], [q[i] + 0.1, q[i] - 0.1], color='black')
    for i in info['ECG_S_Peaks']:
        if not (isinstance(i, float)):
            plt.plot([i, i], [q[i] + 0.1, q[i] - 0.1], color='r')
    for i in info['ECG_T_Peaks']:
        if not (isinstance(i, float)):
            plt.plot([i, i], [q[i] + 0.1, q[i] - 0.1], color='orange')
    for i in info['ECG_Q_Peaks']:
        if not (isinstance(i, float)):
            plt.plot([i, i], [q[i] + 0.1, q[i] - 0.1], color='purple')
    plt.show()
    # nk.ecg_plot(signals, info)
    # fig = plt.gcf()
    # fig.set_size_inches(10, 12, forward=True)
    # fig.savefig('myfig.png')


def aveValue(d, signals):
    c = 0
    s = 0
    for i in d:
        if not (isinstance(i, float)):
            s += signals[i]
            c += 1
    return s / c


def anST(d1, d2, signals):
    s = 0
    c = 0
    q = 0
    for i in range(len(d1)):
        if not (isinstance(d1[i], float)) and not (isinstance(d2[i], float)):
            sup = signals[d1[i] + 5: d2[i]]
            s += sum(sup)/len(sup)
            q += sup[-1] - sup[0]
            c += 1
    return s / c, q / c

def analisECG(k=0):
    result = [0, 0, 0, 0, 0, 0]  # Q, R, S, ST-average value, ST-change, T
    signals = nk.ecg_clean(data[k], sampling_rate=500)
    signals1, info = nk.ecg_delineate(signals, sampling_rate=500)
    signals2, r = nk.ecg_peaks(signals, sampling_rate=500)
    result[0] = aveValue(info['ECG_Q_Peaks'], signals)
    result[1] = aveValue(r['ECG_R_Peaks'], signals)
    result[2] = aveValue(info['ECG_S_Peaks'], signals)
    result[3], result[4] = anST(info['ECG_S_Peaks'], info['ECG_T_Onsets'], signals)
    result[5] = aveValue(info['ECG_T_Peaks'], signals)
    return result

# f2()
# f1()
# f3()


start = time.time()
name = '21682_hr'
with open("task_1/train/" + name + ".npy", "rb") as f:
    data = np.load(f, allow_pickle=True)
print(analisECG(5))
end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")
