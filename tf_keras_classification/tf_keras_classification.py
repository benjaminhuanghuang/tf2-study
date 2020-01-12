import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
import tensorflow as tf
# from tensorflow import keras
import keras

import os
import sys
import time


def show_single_image(img_arr):
  plt.imshow(img_arr, cmap="binary")
  plt.show()

class_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
'Ankel boot']

def show_images(n_rows, n_cols, x_data, y_data, class_name):
  plt.figure(figsize=(n_cols*1.4, n_rows*1.6))
  for row in range(n_rows):
    for col in range(n_cols):
      index = n_cols * row + col
      plt.subplot(n_rows, n_cols, index + 1)
      plt.imshow(x_data[index], cmap="binary", interpolation="nearest")
      plt.axis("off")
      plt.title(class_names[y_data[index]])
  plt.show()


fashion_minst = keras.datasets.fashion_mnist
(x_train_all, y_train_all), (x_test, y_test) = fashion_minst.load_data()

x_valid, x_train = x_train_all[:5000], x_train_all[5000:]
y_valid, y_train = y_train_all[:5000], y_train_all[5000:]

# show_single_image(x_train[0])
show_images(3, 5, x_train, y_train, class_names)


