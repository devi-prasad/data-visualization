from __future__ import division
import numpy as np
import pandas as pd

def read_responses_men(path):
    mpd = pd.DataFrame.from_csv(path, header=None, index_col=None)
    mpd1 = mpd[mpd[1] == 1][1]
    mpd2 = mpd[mpd[1] == 2][1]
    mpd3 = mpd[mpd[1] == 3][1]
    mpd4 = mpd[mpd[1] == 4][1]
    mpd5 = mpd[mpd[1] == 5][1]
    #
    mc = mpd1.size + mpd2.size + mpd3.size + mpd4.size + mpd5.size
    #
    return (mc, mpd1, mpd2, mpd3, mpd4, mpd5)


def read_responses_women(path):
    wpd = pd.DataFrame.from_csv(path, header=None, index_col=None)
    wpd1 = wpd[wpd[1] == 1][1]
    wpd2 = wpd[wpd[1] == 2][1]
    wpd3 = wpd[wpd[1] == 3][1]
    wpd4 = wpd[wpd[1] == 4][1]
    wpd5 = wpd[wpd[1] == 5][1]
    #
    wc = wpd1.size + wpd2.size + wpd3.size + wpd4.size + wpd5.size
    #
    return (wc, wpd1, wpd2, wpd3, wpd4, wpd5)

def make_stat(n, rare, infrq, occ, frq, nosure):
    d = [ np.around(rare/n, 3),
          np.around(infrq/n, 3),
          np.around(occ/n, 3),
          np.around(frq/n, 3), 
          np.around(nosure/n, 3)]
    stat = pd.DataFrame(d, columns=['summary'], index=range(1, 6))
    return stat


def run_test():
    mc, mrare, minfq, mocc, mfrq, mnosure = read_responses_men("men.csv")
    wc, wrare, winfq, wocc, wfrq, wnosure = read_responses_women("women.csv")
    #
    print(mc, mrare.size, minfq.size, mocc.size, mfrq.size, mnosure.size)
    print(wc, wrare.size, winfq.size, wocc.size, wfrq.size, wnosure.size)
    #
    mresp = make_stat(mc, mrare.size, minfq.size, mocc.size, mfrq.size, mnosure.size)
    wresp = make_stat(wc, wrare.size, winfq.size, wocc.size, wfrq.size, wnosure.size)
    #
    print("Response -- men")
    print(mresp)
    print("\n")
    print("Response -- women")
    print(wresp)


run_test()
