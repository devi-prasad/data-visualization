from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def import_data_and_validate(path):
  df = pd.read_csv(path,
            header=0, # the first row is the header
            dtype={'Male':np.int32, 'Female':np.int32, 'Total': np.int32} )
  ##
  assert(all(df.Male + df.Female == df.Total))
  ##
  return df


def compute_stats(df):
  total = df.Male + df.Female
  nm = df.Male/total
  nf = df.Female/total
  mf = nm - nf
  mf.name = 'MF'
  mf.sort_values(inplace=True) # sort in place
  return mf


def plot_crime_gender_pattern(df, mf):
  fig = plt.figure(figsize=(20, 12), dpi=80)
  fig.canvas.set_window_title('Gender Differences in Crime Patterns')
  axes = fig.add_subplot(111)
  fig.canvas.draw()
  #
  axes.set_xlim(-0.5, 1.0)
  axes.set_ylim(0, mf.index.size)
  axes.set_xlabel('PATTERN')
  axes.set_ylabel('OFFENSE')
  axes.spines['right'].set_visible(False)
  axes.spines['top'].set_visible(False)
  axes.spines['left'].set_position(('data', -0.5))
  axes.spines['bottom'].set_position(('data', 0 ))
  axes.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
  axes.yaxis.set_major_locator(ticker.MultipleLocator(1))
  #
  axes.set_yticks(np.linspace(0, mf.index.size-1, mf.index.size, endpoint=True))
  ## to plot an ascending pattern, properly label the y-axis.
  ## labels must match the ascending order of the offense values
  labels = []
  for i in mf.index:
    labels.append(df.Offense.values[i])
  axes.set_yticklabels(labels);
  ##
  plt.grid(True, which='both')
  axes.plot(mf.values, range(len(mf.values)), 'ro')
  plt.show()


def main():
  df = import_data_and_validate('arrests_usa_2014.csv')
  mf = compute_stats(df)
  plot_crime_gender_pattern(df, mf)


main()
