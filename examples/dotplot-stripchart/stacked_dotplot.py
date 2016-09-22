from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

## returns a pd.Series object.
def import_data(path):
  df = pd.read_csv(path,
            header=0, # the first row is the header
            dtype={'SMMAY':np.int32,  'NYMAY':np.int32, 
                   'SMJUNE':np.int32, 'SMJULY':np.int32 } )
  ##
  df1 = df['SMMAY']
  df1.columns = ['oz']
  df2 = df['SMJUNE']
  df2.columns= ['oz']
  df3 = df['SMJULY']
  df3.columns = ['oz']
  dfr = pd.concat([df1, df2, df3], 
                  axis=0, join='inner', ignore_index=True)
  return dfr


## returns a list of positive integers representing the height of the 
##   stack of dots. Index of the array is the point on the x-axis, and the
##   number at that index is the height of the stack of dots.
##
def transform(ps):
  dots = np.zeros(250, dtype=np.int8).tolist()
  for v in ps:
    dots[v] = dots[v] + 1
  #
  return dots

# dots is an array of numbers. Each value gives the stack height.
def dotplot_stacked(dots):
  fig = plt.figure(figsize=(10, 3), dpi=80)
  fig.canvas.set_window_title('Ozone Concentration')
  axes = fig.add_subplot(111)
  #
  axes.set_xlim(0, 250)
  axes.set_ylim(0, 2)
  axes.set_xlabel('OZONE (ppb)')
  axes.spines['right'].set_visible(False)
  axes.spines['top'].set_visible(False)
  axes.spines['left'].set_visible(False)
  axes.set_yticks([]) # no ticks on the y axis
  #
  axes.spines['bottom'].set_visible(True)
  axes.set_xticklabels([0, 50, 100, 150, 200, 250]);
  axes.xaxis.set_minor_locator(ticker.MultipleLocator(10))
  ##
  ## Drawing a stack of dots requires attention to details.
  ## For each point in x-axis we determine the height of the stack of dots and 
  ##   immediately plot.
  ##
  for i in range(1, len(dots)):    # ignore zeroth index
    l = dots[i]
    if l > 0:
      x = (np.zeros(l) + i).tolist()
      y = np.zeros(l) + 0.2
      inc = 0.0
      for j in range(l):
        y[j] = y[j] + inc
        inc = inc + 0.1
      #
      axes.plot(x, y, 'bo')
  ##
  plt.show()


def main():
  df = import_data('ozone.csv')
  dots = transform(df)
  dotplot_stacked(dots)


main()
