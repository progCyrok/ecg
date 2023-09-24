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
    k = 0
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    with open("task_1/train/00669_hr.npy", "rb") as f:
        data3 = np.load(f, allow_pickle=True)
    with open("task_1/train/01223_hr.npy", "rb") as f:
        data4 = np.load(f, allow_pickle=True)
    q = nk.ecg_clean(data3[k], sampling_rate=500)
    signals, info = nk.ecg_delineate(q, sampling_rate=500)
    plt.plot(q)
    # plt.plot(data3[k])
    # print(signals)
    # print(info)
    # for i in info:
    #     print(i, info[i])
    for i in info['ECG_R_Offsets']:
        if not (isinstance(i, float)):
            plt.plot([i, i], [q[i] + 0.1, q[i] - 0.1], color='black')
    for i in info['ECG_S_Peaks']:
        if not (isinstance(i, float)):
            plt.plot([i, i], [q[i] + 0.1, q[i] - 0.1], color='r')
    for i in info['ECG_T_Onsets']:
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
    if c == 0:
        return 0
    return s / c


def anST(d1, d2, signals):
    s = 0
    c = 0
    q = 0
    for i in range(len(d1)):
        if not (isinstance(d1[i], float)) and not (isinstance(d2[i], float)):
            sup = signals[d1[i] + 5: d2[i]]
            if sup.any():
                s += sum(sup) / len(sup)
                q += (sup[-1] - sup[0])
                c += 1
    if c == 0:
        return 0, 0
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
train_gts = pd.read_csv("task_1/train/train_gts.csv")
dict = {'record_name': [],
        'Q1': [], 'R1': [], 'S1': [], 'ST_average_value1': [], 'ST-change1': [], 'T1': [],
        'Q2': [], 'R2': [], 'S2': [], 'ST_average_value2': [], 'ST-change2': [], 'T2': [],
        'Q3': [], 'R3': [], 'S3': [], 'ST_average_value3': [], 'ST-change3': [], 'T3': [],
        'Q4': [], 'R4': [], 'S4': [], 'ST_average_value4': [], 'ST-change4': [], 'T4': [],
        'Q5': [], 'R5': [], 'S5': [], 'ST_average_value5': [], 'ST-change5': [], 'T5': [],
        'Q6': [], 'R6': [], 'S6': [], 'ST_average_value6': [], 'ST-change6': [], 'T6': [],
        'Q7': [], 'R7': [], 'S7': [], 'ST_average_value7': [], 'ST-change7': [], 'T7': [],
        'Q8': [], 'R8': [], 'S8': [], 'ST_average_value8': [], 'ST-change8': [], 'T8': [],
        'Q9': [], 'R9': [], 'S9': [], 'ST_average_value9': [], 'ST-change9': [], 'T9': [],
        'Q10': [], 'R10': [], 'S10': [], 'ST_average_value10': [], 'ST-change10': [], 'T10': [],
        'Q11': [], 'R11': [], 'S11': [], 'ST_average_value11': [], 'ST-change11': [], 'T11': [],
        'Q12': [], 'R12': [], 'S12': [], 'ST_average_value12': [], 'ST-change12': [], 'T12': []}
df = pd.DataFrame(dict)
z = 0

for i in range(len(train_gts['record_name'])):
    # print(i/len(train_gts['record_name']), '%')
    print(i)
    if i == 30:
        continue
    name = train_gts['record_name'][i]
    with open("task_1/train/" + name + ".npy", "rb") as f:
        data = np.load(f, allow_pickle=True)
    newdata = [name]
    for k in range(12):
        try:
            sup = analisECG(k)
        except:
            sup = [0] * 6
        newdata.extend(sup)
    df.loc[len(df.index)] = newdata
print(df)
df.to_csv('file1.csv')
end = time.time()
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
