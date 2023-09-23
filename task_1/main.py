import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f2():
    data1 = pd.read_csv("train/train_meta.csv")
    data2 = pd.read_csv("train/train_gts.csv")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    sr1 = set()
    sr2 = set()
    sr3 = set()
    sr4 = set()

    name = list(data1['record_name'])
    meta = [-1] * len(name)
    for i in range(len(name)):
        df = data2.loc[data2['record_name'] == name[i]]
        meta[i] = df['myocard'].loc[df.index[0]]
    data1['myocard'] = meta
    print(data1[['pacemaker','extra_beats']])

def pandas_add():
    data1 = pd.read_csv("train/train_meta.csv")
    data2 = pd.read_csv("train/train_gts.csv")
    name = list(data1['record_name'])
    meta = [-1] * len(name)
    for i in range(len(name)):
        df = data2.loc[data2['record_name'] == name[i]]
        meta[i] = df['myocard'].loc[df.index[0]]
    data1['myocard'] = meta
    dt = {'record_name':[],'stadium1':[],'stadium2':[],'sex':[],'age':[],'imt':[],'dependence_stadium':[],'validated_by_human':[],
          'pacemaker':[],'myocard':[]}
    dataframe_pandas = pd.DataFrame(dt)
    import funktions
    funk = funktions.Funk()
    for i in range(len(data1['record_name'])):
        arr = []
        arr.append(data1['record_name'][i])
        arr.append(funk.infarction_stadium(data1['infarction_stadium1'][i]))
        arr.append(funk.infarction_stadium(data1['infarction_stadium2'][i]))
        arr.append(funk.sex(data1['sex'][i]))
        arr.append(funk.age(data1['age'][i]))
        arr.append(funk.imt(data1['weight'][i],data1['height'][i]))
        arr.append(funk.dependence_stadium(data1['infarction_stadium1'][i],data1['infarction_stadium2'][i]))
        arr.append(funk.validated_by_human(data1['validated_by_human'][i]))
        arr.append(funk.pacemaker(data1['pacemaker'][i]))
        arr.append(data1['myocard'][i])
        dataframe_pandas.loc[len(dataframe_pandas.index)] = arr
    dataframe_pandas.to_csv('file_without_anilise_of_graphics.csv')

pandas_add()