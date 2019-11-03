import keras
import tensorflow as tensor

# Model Creation as specified in https://www.tensorflow.org/tutorials/keras/save_and_load

dataset = tensor.keras.datasets.mnist # Dataset of Handwritings
(train_x, train_y), (test_x, test_y) = dataset.load_data()
train_x = tensor.keras.utils.normalize(train_x, axis = 1)
test_x = tensor.keras.utils.normalize(test_x, axis = 1)

for train in range(len(train_x)):
    for row in range(28):
        for col in range(28):
            if train_x[train][row][col] != 0:
                train_x[train][row][col] = 1

model = tensor.keras.models.Sequential()
model.add(tensor.keras.layers.Flatten())
model.add(tensor.keras.layers.Dense(128, activation = tensor.nn.relu))
model.add(tensor.keras.layers.Dense(10, activation = tensor.nn.softmax))

model.compile(
    optimize = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics= ['accuracy']
)

model.fit(train_x, train_y, epochs = 10)
model.save('number.model')

print("A Model has been generated and stored on your computer")