#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sohel
#
# Created:     19/05/2025
# Copyright:   (c) sohel 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def dtep_function(value):
  if value >= 0:
    return 1
  else:
    return 0

class perceptron:
  def __init__(self, learning_rate=0.1, epochs=1):
    self.weights = [0, 0, 0]
    self.bias = 0
    self.learning_rate = learning_rate
    self.epochs = epochs

  def step_function(self, x):
    return 1 if x >= 0 else 0

  def predict(self, inputs):
    summation = sum(i * w for i, w in zip(inputs, self.weights)) + self.bias
    return self.step_function(summation)

  def train(self, training_inputs, labels):
    for epoch in range(self.epochs):
      print(f"Epoch {epoch+1}")
      for inputs, label in zip(training_inputs, labels):
        prediction = self.predict(inputs)
        error = label - prediction
        for i in range(len(self.weights)):
          self.weights[i] += self.learning_rate * error * inputs[i]
        self.bias += self.learning_rate * error
        print(f"Inputs: {inputs}, Target: {label}, Prediction: {prediction}, Error: {error}")
      print(f"Weights: {self.weights}, Bias: {self.bias}\n")


training_inputs = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 0],
    [0, 1, 1]
]
labels = [0, 1, 1, 0, 1, 1]

p = perceptron()
p.train(training_inputs, labels)

print("Testing trained Perceptron:")
for inputs in training_inputs:
  print(f"Input: {inputs}, Output: {p.predict(inputs)}")