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
model = Sequential()
# Add a single dense layer with one neuron
model.add(Dense(1, input_dim=80, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(x, y, epochs=1000, batch_size=4, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f"Loss: {loss}, Accuracy: {accuracy}")
model.save("first_model_save")
