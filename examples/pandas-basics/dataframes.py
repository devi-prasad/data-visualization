import numpy as np
import pandas as pd

def dataframe_default_indices():
  data = [[1, 2, 3],
          [10, 20, 30],
          [100, 300, 400],
          [1000, 2000, 3000],
          [10000, 20000, 30000]]
  ##
  df = pd.DataFrame(data, columns=['a', 'b', 'c'])
  ##
  f = df.first_valid_index()
  l = df.last_valid_index()
  assert(f == 0 and l == 4)


def dataframe_custom_indices():
  data = [[1, 2, 3],
          [10, 20, 30],
          [100, 300, 400],
          [1000, 2000, 3000],
          [10000, 20000, 30000]]
  ##
  df = pd.DataFrame(data, columns=['a', 'b', 'c'])
  ##
  df.index = list('PQRST')
  f = df.first_valid_index()
  l = df.last_valid_index()
  assert(f == 'P' and l == 'T')


### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# iterate over each row as an (index, vals) pairs
# vals is usually an instance of pd.series of values of variables (columns)
# this is repeated for each row in the data frame
def apply_on_rows(df, f):
    itr = df.iterrows()
    for (i, r) in itr:
        f(r)

def project_cols_apply_on_rows(df, cols, f):
    apply_on_rows(df[cols], f)

# DataFrame.apply applies f on each column values
def apply_on_columns(df, f):
    df.apply(f)

## a simple function to view the row (meta)data
def prcol(col):
    print(type(col), 'name: ', col.name, 'vals: ', col.values)

def prrow(row):
	print(type(row), 'name: ', row.name, 'vals: ', row.values)

apply_on_rows(df, prrow)

apply_on_columns(df, prcol)

### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

###
## Captures the 'blend' operation from the Grammar of Graphics
## ignores the indices on the data sets
## the resulting data frame will have plain numerical indices
###
def append_ignore_index_same_columns():
    datasetA = [[1, 2, 3], [10, 20, 30]]
    datasetB = [[100, 300, 400], [1000, 2000, 3000], [10000, 20000, 30000]]

    # notice that both data sets are based on the same variables.
    dfA = pd.DataFrame(datasetA, columns=['a', 'b', 'c'])
    dfB = pd.DataFrame(datasetB, columns=dfA.columns)
    # ---
    dfAB = dfA.append(dfB, ignore_index=True, verify_integrity=True)
    dfBA = dfB.append(dfA, ignore_index=True, verify_integrity=True)
    # ---
    assert(dfAB.size == dfA.size + dfB.size)
    assert(dfAB.size == dfBA.size)
    # must add 1 because indexes are zero-based.
    assert(dfAB.last_valid_index() == 1 + dfA.last_valid_index() +
           dfB.last_valid_index())

### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

###
## blend operation from the Grammar of Graphics.
## The resulting data frame includes indices from source data frames.
###
def append_merge_index_same_columns():
  datasetA = [[1, 2, 3], [10, 20, 30]]
  datasetB = [[100, 300, 400], [1000, 2000, 3000], [10000, 20000, 30000]]
  ##
  dfA = pd.DataFrame(datasetA, columns=['a', 'b', 'c'])
  dfB = pd.DataFrame(datasetB, columns=dfA.columns)
  ##
  ## notice the way we set new indices
  dfA.index = ['key1', 'key2']
  dfB.index = ['keyX', 'keyY', 'keyZ']
  ## 
  dfAB = dfA.append(dfB, verify_integrity=True)
  ##
  assert(dfA.index.intersection(dfB.index).size == 0)
  assert(((dfA.index | dfB.index) == dfAB.index).all())

### +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def project_dataframe_columns():
  datasetA = [[1, 2, 3], [10, 20, 30]]
  datasetB = [[100, 300, 400], [1000, 2000, 3000], [10000, 20000, 30000]]
  ##
  dfA = pd.DataFrame(datasetA, columns=['a', 'b', 'c'])
  dfB = pd.DataFrame(datasetB, columns=['a', 'b', 'c'])
  dfNew = dfA[ ['c', 'a'] ]
  ###
  ##     | c    a 
  ##   0 | 3    1
  ##   1 | 30  10
  ###
  dfNew['b'] = dfB['b']
  ###
  ##     | c    a     b  
  ##   0 | 3    1   300
  ##   1 | 30  10  2000 
  ### 
  assert(dfNew.index.size == 2)
  assert(dfNew['c'][0] == 3)
  assert(dfNew['b'][1] == 2000)
  assert(dfNew['a'][0] == 1 and dfNew['a'][1] == 10)


def cross_dataframe_aligned_indices():
  df = pd.DataFrame([10, 20, 30, 40, 50], columns=['a'])
  df.index = [list('pqrst')]
  df2 = pd.DataFrame([111, 222, 333, 444, 555], columns=['a'])
  df2.index = [list('pqrst')]
  dfNew['a'] = df['a']
  dfNew['b'] = df2['a']
###
##    |   b   a
##  p | 111  10
##  q | 222  20
##  r | 333  30
##  s | 444  40
##  t | 555  50
###
  assert(dfNew['a']['p'] == 10)
  assert(dfNew['b']['t'] == 555)


def cross_dataframe_unaligned_indices():
  df = pd.DataFrame([10, 20, 30, 40, 50], columns=['a'])
  df.index = [list('pqrst')]
  df2 = pd.DataFrame([111, 222, 333, 444, 555], columns=['a'])
  df2.index = [list('rstpq')]
  dfNew['a'] = df['a']
  dfNew['b'] = df2['a']
  ###
  ##    |   b   a
  ##  p | 444  10
  ##  q | 555  20
  ##  r | 111  30
  ##  s | 222  40
  ##  t | 333  50
  ###
  assert(dfNew['a']['p'] == 10)
  assert(dfNew['b']['t'] == 333)
  assert(dfNew['b']['r'] == 111)


def cross_dataframe_unaligned_indices():
  df = pd.DataFrame([10, 20, 30, 40, 50], columns=['a'])
  df.index = [list('pqrst')]
  df2 = pd.DataFrame([111, 222, 333, 444, 555], columns=['b'])
  df2.index = [list('rstpq')]
  dfNew['a'] = df['a']
  dfNew['b'] = df2['b']
  ###
  ##    |   b   a
  ##  p | 444  10
  ##  q | 555  20
  ##  r | 111  30
  ##  s | 222  40
  ##  t | 333  50
  ###
  assert(dfNew['a']['p'] == 10)
  assert(dfNew['b']['t'] == 555)

