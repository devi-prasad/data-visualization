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
  fig = plt.figure()
  fig.canvas.set_window_title('Gender Differences in Crime Patterns')
  axes = fig.add_subplot(111)
  fig.canvas.draw()
  #
  axes.set_title("Gender Differences in Crime Patterns")
  axes.set_xlim(-0.5, 1.0)
  axes.set_ylim(mf.index.size)
  axes.set_xlabel('PATTERN')
  axes.set_ylabel('OFFENSE')
  axes.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
  axes.yaxis.set_major_locator(ticker.MultipleLocator(1))
  locs = axes.get_yticks().tolist()
  axes.set_yticks(locs)
  axes.set_yticklabels(df.Offense.values)
  #
  plt.grid(True, which='both')
  axes.plot(mf.values, mf.index, 'ro', color='r')
  plt.show()


def main():
  df = import_data_and_validate('arrests_usa_2014.csv')
  mf = compute_stats(df)
  plot_crime_gender_pattern(df, mf)

