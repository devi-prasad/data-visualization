import numpy as np
import pandas as pd

def read_csv_and_sum():
    df = pd.read_csv("data.csv",
                     delim_whitespace=True, 
                     dtype={'v1': np.int32, 'v2': np.int32})
##
    dfsum = pd.DataFrame({'sum' : df['v1'] + df['v2']})
    dfsum.index = df['id']
    print(dfsum)


def read_csv_date_and_sum():
    df = pd.read_csv("data-date.csv",
                     delim_whitespace=True, 
                     parse_dates=[3],
                     infer_datetime_format=True,
                     dtype={'v1': np.int32, 'v2': np.int32})
##
    dfsum = pd.DataFrame({'sum' : df['v1'] + df['v2'], 'date': df.date})
    dfsum.index = df['id']
    print(dfsum)

    sorted_dates = df['date'].sort_values()
    print(sorted_dates)


def read_csv_usecols_and_sum():
    df = pd.read_csv("data-date.csv",
                     delim_whitespace=True, 
                     usecols=[0, 1, 2],
                     dtype={'v1': np.int32, 'v2': np.int32})
##
    dfsum = pd.DataFrame({'sum' : df['v1'] + df['v2']})
    dfsum.index = df['id']
    print(dfsum)
    # print(df)


def mock_csv():
    from io import StringIO
    #from StringIO import StringIO
    data=u'v1,v2\n1,-2\n2,4\n10,20\n30,40\n50,60\n-70,80\n90,-100'
    df = pd.read_csv(StringIO(data), dtype={'v1': np.int8, 'v2': np.int8})
    dfsum = pd.DataFrame({'sum' : df.v1 + df.v2})
    print(dfsum)

mock_csv()

