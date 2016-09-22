import pandas as pd

failed = []

def show_freq_sort():
  df = pd.read_csv('frequencies.csv',
                   names=['email_id', 'frequency'],
                   index_col=['email_id'])
  ##
  sortedfreq = df.sort_values('frequency')
  ##
  ##
  itr = sortedfreq.iterrows()
  for (i, r) in itr:
    emid = r.name
    freq = r.frequency
    try:
      id,domain = emid.split('@')
      emid = id[:4] + '...@' + domain
      print emid.rjust(32), ' ', freq
    except ValueError:
  	  failed.append((emid, freq))


def show_failed():
  if len(failed) > 0:
    print "\n\n\n"
    for id in failed:
      print id


show_freq_sort()
#show_failed()
