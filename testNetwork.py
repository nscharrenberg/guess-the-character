import keras
import tensorflow as tensor
import numpy as nmp
import matplotlib.pyplot as plt

dataset = tensor.keras.datasets.mnist # Dataset of Handwritings
(train_x, train_y), (test_x, test_y) = dataset.load_data()
train_x = tensor.keras.utils.normalize(train_x, axis = 1)
test_x = tensor.keras.utils.normalize(test_x, axis = 1)

for train in range(len(train_x)):
    for row in range(28):
        for col in range(28):
            if train_x[train][row][col] != 0:
                train_x[train][row][col] = 1

model_name = 'number.model'
model = tensor.keras.models.load_model(model_name)
iterations = 50
predictions = model.predict(test_x[:iterations])

count = 0

for number in range(len(predictions)):
    actual = test_y[number]
    guess = (nmp.argmax(predictions[number]))

    print("The number you wrote is: ", actual, " but the Neural Network guessed: ", guess)

    if(guess != actual):
        count += 1

    plt.imshow(test_x[number], cmap = plt.cm.binary)
    plt.show()

print(count, " wrong guesses out of ", len(test_x))
percentage = 100 - ((count / len(test_x)) * 100)
print(str(percentage), "% of the guesses was correct")


