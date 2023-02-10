import random

import numpy as np
import tensorflow as tf

inputs = tf.keras.Input(shape=[3]) #x, y, angle
x = tf.keras.layers.Dense(16)(inputs)
#x = tf.keras.layers.Dense(16)(x)
forward = tf.keras.layers.Dense(1, activation="sigmoid")(x)
angle = tf.keras.layers.Dense(1, activation="tanh")(x)

model = tf.keras.models.Model(inputs=inputs, outputs=[forward, angle], name="UnitV1")
model.summary()

#print(model.get_weights())

MUTATION = 0.1

weights = model.get_weights()
weights = [w + random.uniform(-MUTATION, MUTATION) for w in weights]
model.set_weights(weights)

#print(model.get_weights())

result = model.predict([[12, 13, 5]])
print(result)
print(result[0][0][0])
print(result[1][0][0])