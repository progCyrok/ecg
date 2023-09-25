import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f2():
    data1 = pd.read_csv(r"C:\Users\gosha\ecg\task_1\test\test_meta.csv")
    data2 = pd.read_csv(r"C:\Users\gosha\ecg\task_1\test\test_gts.csv")
    name = list(data1['record_name'])
    meta = [-1] * len(name)
    for i in range(len(name)):
        df = data2.loc[data2['record_name'] == name[i]]
        meta[i] = df['myocard'].loc[df.index[0]]
    data1['myocard'] = meta


def pandas_add():
    data1 = pd.read_csv(r"C:\Users\gosha\ecg\task_1\test\test_meta.csv")
    data2 = pd.read_csv(r"C:\Users\gosha\ecg\task_1\test\test_gts.csv")
    name = list(data1['record_name'])
    meta = [-1] * len(name)
    for i in range(len(name)):
        df = data2.loc[data2['record_name'] == name[i]]
        meta[i] = df['myocard'].loc[df.index[0]]
    data1['myocard'] = meta
    dt = {'record_name':[],'stadium1':[],'stadium2':[],
          'sex':[],'age':[],'imt':[],'dependence_stadium':[],
          'validated_by_human':[], 'pacemaker':[],
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
          'Q12': [], 'R12': [], 'S12': [], 'ST_average_value12': [], 'ST-change12': [], 'T12': [],
          'miocard': [],
          }
    dataframe_pandas = pd.DataFrame(dt)
    import funktions
    funk = funktions.Funk()
    stroka = pd.read_csv(r"C:\Users\gosha\ecg\test_data.csv", delimiter= ',')
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
        try:
            for num in range(len(data1['record_name'])):
                if data1['record_name'][i] == stroka['record_name'][num]:
                    """в первых двух храниться id и название """
                    for j in stroka.iloc[i][stroka.columns.tolist()[2:]]:
                        arr.append(j)
                    arr.append(data1['myocard'][i])
                    dataframe_pandas.loc[len(dataframe_pandas.index)] = arr
                    break
        except Exception as e:
            print(e)

    dataframe_pandas.to_csv('test_data.csv')

pandas_add()