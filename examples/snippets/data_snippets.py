### Data
### (pandas reference, pp 615)

###
import pandas as pd
import numpy as np
###

ones = np.ones(5, dtype=np.int32)
zs = np.zeros(5, dtype=np.int32)
emp = np.empty(5, dtype=np.int32)
arr = np.array(5, dtype=np.int32)

emp = np.empty((2, 2), dtype=np.int32)
zs = np.zeros((3, 5), dtype=np.int32)

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###  numpy.arange([start, ] stop, [step, ] dtype=None)
###  creates an interval that is closed on the left a and open on the right.
### 
np.arange(10, dtype=np.int32) # np.array[0, ..., 9]
np.arange(10, 100, 7)
np.arange(-0.2, 0.5, 0.1, dtype=np.float) 
# ==> np.array([-0.2, -0.1, 0., 0.1, 0.2, 0.3, 0.4])

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
np.cumsum([0.30, 0.15, 0.10, 0.07, 0.38])
np.cumsum([0.08, 0.11, 0.17, 0.32, 0.32])

np.cumsum([range(10)])
np.cumsum([range(1,10)])

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# np.unique(ar, return_index=False, return_inverse=False, return_counts=False)
# np.union1d(ar1, r2) 
# np.intersect1d(ar1, ar2, assume_unique=False)
# np.setdiff1d(ar1, ar2, assume_unique=False)

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
### Return evenly spaced numbers over a specified interval.
### Returns num evenly spaced samples
### interval is calculated over the closed interval [start, stop].
### The endpoint of the interval can optionally be excluded.

np.linspace(10, 20, num=11)

np.linspace(0.1, 0.2, num=5)
## ==> array([ 0.1, 0.125, 0.15, 0.175, 0.2 ])

np.linspace(0.1, 0.2, num=5, endpoint=False)
## ==> array([ 0.1, 0.12, 0.14, 0.16, 0.18])

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
map(np.abs, map(np.int, np.ceil(np.random.randn(10) * 20)))
np.random.random_integers(-10, 100, 15)
min(np.random.random_integers(-10, 100, 15))
max(np.random.random_integers(-10, 100, 15))

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
### NumPy arrays

np.random.rand()    # single random number
np.random.rand(4)   # array of four random numbers
np.random.rand(3, 4)
  ## 3 rows, 4 cols each
np.random.rand(3, 4, 2)
  ## 3 instances of 4 rows of 2 cols each

np.random.sample(10)
np.random.random(10)

np.random.permutation([10, 20, 30, 40, 50]) # returns a permutation

np.random.shuffle([10, 20, 30, 40, 50]) # in place shuffle - mutates the array

ar = np.array(range(24), dtype=np.int16)
assert(ar.ndim == 1 and ar.size == 24)

ar64 = ar.reshape(6, 4)
assert(ar64.ndim == 2 and ar64.size == 24)
assert(ar.ndim == 1 and ar.size == 24)

ar234 = ar.reshape(2, 3, 4)
assert(ar234.ndim == 3 and ar64.size == 24)

ar234 = ar.reshape(2, 3, -1)
assert(ar234.ndim == 3 and ar64.size == 24)

assert((ar.reshape(2, 3, 4) == ar.reshape(2, 3, -1)).all())

ar[4:10]  # slice
ar[ [1, 3, 5, 7, 11] ] # indices


##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
### pandas Series
#
## Series(data, index, dtype) # index aka axes labels
## Series.append(ps, verify_integrity=False)

psvals = pd.Series({'vals': np.random.random_integers(1, 400, 50)})

psabc = pd.Series({'a': [1, 2, 3], 'b': 10, 'c': 100})

sta = pd.Series(
           ['FORTRAN',	'COBOL', 'Algol', 'Pascal', 'C', 'C++', 'Java', 'go'],
           index = ['f', 'cobol', 'al', 'p', 'c', 'cpp', 'j', 'go'])

ar42 = sta.reshape(4, 2)
assert(sta.ndim == 1 and ar42.shape == (4, 2))

dyn = pd.Series(['Python', 'JavaScript', 'Ruby', 'PHP', 'Pyret'], dtype=str)
dyn.set_axis(0, ['p', 'j', 'r', 'php', 'pyret'])
assert(dyn.php == 'PHP')

sta.append(dyn)
try:
  sta.append(sta, True)
except:
  None
sta.append(sta, False)

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

df = pd.DataFrame({'vals':[1, 2, 3, 4, -7, 0]}, dtype=np.int16)
dftwice = df * 2
dfplus2 = df + 2
dfsqr = df * df

df * 2 == df + df

5 * (df + df) == (df + df) * 5
(df + df) * 5 == df * 5 + df * 5
df.iloc[5] == 0
df.iloc[0] == 1

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
imp = pd.DataFrame({'langs': np.array(['Algol', 'FORTRAN', 'C', 'C++', 'Java'], 
                   dtype=str)})
fun = pd.DataFrame({'langs': np.array(['Haskell', 'ML', 'OCaml'],
                   dtype=str)})
dyn = pd.DataFrame({'langs': np.array(['Python', 'JavaScript', 'Ruby', 'PHP'], 
                   dtype=str)})
all = pd.concat([imp, fun, dyn], ignore_index=True)
sorted = all.sort_values('langs')
sorted.langs.values # numpy.ndarray

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

imp = pd.DataFrame({'langs': np.array(['Algol', 'FORTRAN', 'C', 'C++', 'Java'], 
                                      dtype=str),
                    'years':np.array([1960, 1950, 1970, 1990, 1995]) })
fun = pd.DataFrame({'langs': np.array(['Haskell', 'ML', 'OCaml'],
                                      dtype=str),
                    'years':np.array([1992, 1970, 1990]) })
dyn = pd.DataFrame({'langs': np.array(['Python', 'JavaScript', 'Ruby', 'PHP'], 
                                      dtype=str),
                    'years':np.array([1995, 1996, 1990, 1990]) })

all = pd.concat([imp, fun, dyn], ignore_index=True)

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

imp = pd.DataFrame({'langs': np.array(['Algol', 'FORTRAN', 'C', 'C++', 'Java'], 
                                      dtype=str),
                    'years': np.array([1960, 1950, 1970, 1990, 1995], 
                                      dtype=pd.datetime),
                    'type':'imperative' })


##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

df = pd.DataFrame({'pos': np.array([0, 1, 2, 3, 4, 5], dtype=np.int8)})

pd.concat([df, df], ignore_index=True)
pd.concat([df, df], ignore_index=False)
df = pd.DataFrame({'pos': np.array([0, 1, 2, 3, 4, 5], dtype=np.int8),
                   'neg': np.array([-1, -2, -3, -4, -5, -6], dtype=np.int32) 
                 })

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
df1 = pd.DataFrame(
            {'A': ['A0', 'A1', 'A2', 'A3'],
             'B': ['B0', 'B1', 'B2', 'B3'],
             'C': ['C0', 'C1', 'C2', 'C3'],
             'D': ['D0', 'D1', 'D2', 'D3']
            },
            index=[0, 1, 2, 3]
            #index=[1, 2, 3, 4]
      )

df2 = pd.DataFrame(
          {'A': ['A4', 'A5', 'A6', 'A7'],
           'B': ['B4', 'B5', 'B6', 'B7'],
           'C': ['C4', 'C5', 'C6', 'C7'],
           'D': ['D4', 'D5', 'D6', 'D7'],
           'E': ['E1', 'E2', 'E3', 'E4']
          },
          index=[4, 5, 6, 7]
          #index=[1, 2, 3, 4]
    )

df3 = pd.DataFrame(
          {'A': ['A8', 'A9', 'A10', 'A11'],
           'B': ['B8', 'B9', 'B10', 'B11'],
           'C': ['C8', 'C9', 'C10', 'C11'],
           'D': ['D8', 'D9', 'D10', 'D11']
          },
          index=[8, 9, 10, 11]
          #index=[1, 2, 3, 4]
    )


#(1)
##  Notice that the indices of each data frame is unique.
##  Execute the following and check the result.

pd.concat([df1, df2, df3])

#(2)
## Check what happens if we pass
##    index = [1, 2, 3, 4]
## while creating the instances, df1 and df2.

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

df75 = pd.DataFrame(
        {'A': ['A4', 'A5', 'A6', 'A7', 'A8'],
         'B': ['B4', 'B5', 'B6', 'B7', 'B8'],
         'C': ['C4', 'C5', 'C6', 'C7', 'C8'],
         'D': ['D4', 'D5', 'D6', 'D7', 'D8'],
         'E': ['E4', 'E5', 'E6', 'E7', 'E8'],
         'F': ['F4', 'F5', 'F6', 'F7', 'F8'],
         'Z': ['Z4', 'Z5', 'Z6', 'Z7', 'Z8']
        },
        index=[4, 5, 6, 7, 12]
      )

df22 = pd.DataFrame(
      {'A': ['AA4', 'AA5', 'AA6', 'AA7'],
       'B': ['BB4', 'BB5', 'BB6', 'BB7'],
       'C': ['CC4', 'CC5', 'CC6', 'CC7'],
       'D': ['DD4', 'DD5', 'DD6', 'DD7'],
       'E': ['EE4', 'EE5', 'EE6', 'EE7']
      },
      index=[4, 5, 6, 12],
      columns=['C', 'A', 'E']
    )
