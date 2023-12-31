# -*- coding: utf-8 -*-
"""fundamentos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g6Vvi4z7EapWpFDADCYxxY9ADWIZeYho
"""

Define las listas xs y ys con los datos de la secuencia numérica que tienes.
import tensorflow as tf
import numpy as np
# Parámetros del modelo
m = tf.Variable(0.0)
b = tf.Variable(0.0)

# Definición del modelo
def linear_regression(x):
    return m * x + b
# Función de pérdida (Mean Squared Error)
def mean_squared_error(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# Optimizador (Gradient Descent)
optimizer = tf.optimizers.SGD(learning_rate=0.01)
def train_step(x, y):
    with tf.GradientTape() as tape:
        y_pred = linear_regression(x)
        loss = mean_squared_error(y, y_pred)
    gradients = tape.gradient(loss, [m, b])
    optimizer.apply_gradients(zip(gradients, [m, b]))

# Entrenamiento del modelo
for epoch in range(num_epochs):
    train_step(xs, ys)
predicted_ys = linear_regression(xs)
import matplotlib.pyplot as plt

plt.scatter(xs, ys, label="Datos originales")
plt.plot(xs, predicted_ys, color='red', label="Regresión Lineal")
plt.xlabel("Valores de xs")
plt.ylabel("Valores de ys")
plt.legend()
plt.show()
losses = []

# Dentro del ciclo de entrenamiento:
    # ...
    losses.append(loss)

plt.plot(losses)
plt.xlabel("Épocas")
plt.ylabel("Pérdida")
plt.title("Comportamiento de la Precisión en función de la Pérdida")
plt.show()