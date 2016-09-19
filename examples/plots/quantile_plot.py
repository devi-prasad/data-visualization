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
  #
  plt.show()


def compute_perceptual_exponent_quantile():
  data = pd.Series(
    [ 58, 63, 69, 72, 74, 79,
      88, 88, 90, 91, 93, 94,
      97, 97, 99, 99, 99, 100,
      103, 104, 105, 107, 118, 127
    ], dtype=np.int8)
  #
  n = len(data)
  quantile = data.quantile(np.linspace(0, 1, n))
  return quantile


def quantile_plot():
  quantile = compute_perceptual_exponent_quantile()
  draw_quantile_plot(quantile)


quantile_plot()
