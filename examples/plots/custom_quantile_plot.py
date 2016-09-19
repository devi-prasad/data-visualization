from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def draw_quantile_plot(quantile):
  fig = plt.figure()
  fig.canvas.set_window_title('Quantile Plot of Perceptual Exponent')
  #
  axes = fig.add_subplot(111)
  axes.set_title("Quantile Plot")
  axes.set_xlim(0.0, 1.0)
  axes.set_ylim(50, 130)
  axes.set_xlabel('FRACTION OF DATA')
  axes.set_ylabel('QUANTILE Q(p) OF EXPONENT DATA')
  #
  quantile.plot(ax=axes)
  

def compute_perceptual_exponent_quantile(data):
  n = len(data)
  return data.quantile(np.linspace(0, 1, n))


def compute_perceptual_exponent_quantile_custom(data):
  n = len(data)
  # we will include .0 and 1.0 too in the probabilities
  p = range(n+2)
  for i in range(1, 25):
    p[i] = (i - 0.5)/n
  #
  ## extend the probabilities to include .0 and 1.0
  p[0] = 0
  p[n+1] = 1.0
  #
  ## extend data at both ends...
  data = [data[0]] + data + [data[n-1]]
  return pd.Series(data, index=p)


def quantile_plot():
  nums = [ 
    58, 63, 69, 72, 74, 79,
    88, 88, 90, 91, 93, 94,
    97, 97, 99, 99, 99, 100,
    103, 104, 105, 107, 118, 127
  ]
  data = pd.Series(nums, dtype=np.int8)
  quantile = compute_perceptual_exponent_quantile(data)
  draw_quantile_plot(quantile)
  quantile = compute_perceptual_exponent_quantile_custom(nums)
  draw_quantile_plot(quantile)
  #
  plt.show()


quantile_plot()
