from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd

# Define the input data

data = pd.read_csv('file_without_anilise_of_graphics.csv')
"""тк в первой id во второй имя в последнем диагноз"""
x = np.array(data[data.columns.tolist()[2:-1]])
# Define the corresponding output data
y = np.array(data['miocard'])
#
# # Define the model
from tensorflow import keras
from tensorflow.keras import layers

# Создание модели перцептрона
model = keras.Sequential()

# Добавление слоев в модель
model.add(layers.Dense(32, input_dim=80, activation='relu'))  # Скрытый слой с 32 нейронами и функцией активации ReLU
model.add(layers.Dense(1, activation='sigmoid'))  # Выходной слой с 1 нейроном и функцией активации Sigmoid

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучение модели
model.fit(x, y, epochs=1000, batch_size=32)

# Оценка модели
loss, accuracy = model.evaluate(x, y)
print(f'Loss: {loss}')
print(f'Accuracy: {accuracy}')
model.save("my_model.keras")