# guess-the-number
A simple prototyping project for a Neural Network that guesses the number you draw

# Used Tools
- Python 3
- Pygame
- Numpy
- Matplotlib
- Tensorflow
- Keras
- virtualenv (optional)

# Why was this created?
In order to gain more knowledge about Neural Networks and TensorFlow, i wanted to make a simple application where I could learn the basics of a neural network and to get started with TensorFlow.

# The Concept of Guess the Number
The concept is simple, you draw a number and the neural network will try to guess what number you wrote down.

# Installation Guide
`python` is referenced as the for your `python3` alias. This may be either `python` or `python3` depending on how it is setup.

1. Have Python3 installed
2. Have all the required packages installed (Pygame, numpy, matplotlib, tensorflow, keras)  
    I'd also recommend using virtualenv, but it's not required to use.
3. run `python generateModel.py`
    This created a file named `number.model` in your app directory, which will be used during testing and on the canvas.

You are now able to either run the test script or start drawing yourself.

In order to run the test script use `python testNetwork.py`.  
In order to draw yourself run the canvas by running `python canvas.py`.


# Adjusting Values
## Generating Model
In the `generateModel.py` script the only value recommended to change is the `epochs` value.  
Default `epochs` value is `20`.

```python
model.fit(train_x, train_y, epochs = 20)
```

## Testing Network
In the `testNetwork.py` script the only value recommended to change is the `iterations` value.  
Default `iterations` value is `50`.

```python
iterations = 50
predictions = model.predict(test_x[:iterations])
```

## Manually Drawing
In the `canvas.py` script the following values can be changed.
`width`, `height`, `scale`, `background_color`, `pencil_color`.

- When adjusting `width`, `height`, and `scale` make sure the the outcome of `width / scale` and `height / scale` remain with the outcome of `28`, or the application may crash, as the dataset only contains images of `28` pixels.
- `background_color` and `pencil_color` can both be changed, however make sure to stick to RGB e.g `255,0,0` = red.

## Value adjustable on all of the above
On `generateModel.py`, `testNetwork.py` and `canvas.py` you are able to change the `model_name` variable.  
The `model_name` can be changed accordingly to how your generated model name is called. Default is `number.model`.  

Make sure the `model_name` variable is the same on all 3 files.

# Todo list
- [x] Manually draw a character
- [x] Use dataset and make a neural network guess the character you drew.
- [x] Test script to bulk test the neural network.
- [x] Support numbers
- [ ] Support alphabet
- [ ] Support animal drawings


