import numpy as np
import pandas as pd

def make_random_responses(total, rare, infrqnt, occasional, frqnt, notsure):
    assert(total > 0)
    r      = np.ones(rare, dtype=np.int8) 
    infrq  = np.zeros(infrqnt, dtype=np.int8)    + 2
    occ    = np.zeros(occasional, dtype=np.int8) + 3
    frq    = np.zeros(frqnt, dtype=np.int8)      + 4
    nosure = np.zeros(notsure, dtype=np.int8)    + 5
    #
    allres = np.concatenate((r, infrq, occ, frq, nosure))
    np.random.shuffle(allres)
    np.random.shuffle(allres)
    np.random.shuffle(allres)
    return allres

def make_responses_men(path):
    mres = make_random_responses(2838, 851, 426, 284, 199, 1078)
    assert(mres.size == 2838)
    men = pd.Series(mres, index=np.ones(mres.size, dtype=np.int16))
    men.to_csv(path)

def make_responses_women(path):
    wres = make_random_responses(997, 80, 110, 169, 319, 319)
    assert(wres.size == 997)
    women = pd.Series(wres, index=np.zeros(wres.size, dtype=np.int16) + 2)
    women.to_csv(path)


make_responses_men("men.csv")
make_responses_women("women.csv")
