import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("train/train_meta.csv")
with pd.option_context("display.max_rows", None, "display.max_columns", None):
    print(data.head(5))



# with open("test/01165_hr.npy", "rb") as f:
#      data1 = np.load(f, allow_pickle=True)
#
# with open("test/10716_hr.npy", "rb") as f:
#     data2 = np.load(f, allow_pickle=True)
