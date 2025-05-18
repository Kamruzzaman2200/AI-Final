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
  def __init__(self, learning_rate=0.1, epochs=10):
    self.x1 = [0, 0]  # weights for inputs
    self.x3 = 0       # bias
    self.learning_rate = learning_rate
    self.epochs = epochs

  def step_function(self, x):
    return 1 if x >= 0 else 0

  def predict(self, inputs):
    summation = inputs[0] * self.x1[0] + self.x1[1] * inputs[1] + self.x3
    return self.step_function(summation)

  def train(self, training_inputs, labels):
    for epoch in range(self.epochs):
      print(f"Epoch {epoch+1}")
      for inputs, label in zip(training_inputs, labels):
        prediction = self.predict(inputs)
        error = label - prediction
        self.x1[0] += self.learning_rate * error * inputs[0]
        self.x1[1] += self.learning_rate * error * inputs[1]
        self.x3 += self.learning_rate * error
        print(f"Inputs: {inputs}, Target: {label}, Prediction: {prediction}, Error: {error}")
      print(f"Weights: {self.x1}, Bias: {self.x3}\n")

# AND gate training
training_inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
labels = [0, 0, 0, 1]

p = perceptron()
p.train(training_inputs, labels)

print("Testing trained Perceptron:")
for inputs in training_inputs:
  print(f"Input: {inputs}, Output: {p.predict(inputs)}")