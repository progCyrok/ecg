import numpy as np
import pandas as pd
from keras.models import load_model

model = load_model(r'C:\Users\gosha\ecg\task_1\my_model.h5')
data = pd.read_csv(r"C:\Users\gosha\ecg\task_1\test_data.csv")
x = np.array(data[data.columns.tolist()[2:-1]])
a = 0
predictions = model.predict(x)
s = 0
def relu(pred):
    if pred > 0.2:
        return 1
    return 0
for i,pred in enumerate(predictions):
    if relu(pred) == data['miocard'][i]:
        s += 1

print(s/len(x))