# Brownian motion.

import numpy as np
import matplotlib.pyplot as plt

def mean(my_list):
    ans = 0
    for i in my_list:
        ans += i
    return ans/len(my_list)


def brown(n):
    # return and plot a brownian motion sequence with n items.
    # if you want 0,1,2,3,4,.....,10 then you have to n=11 e.g
    br = np.zeros(n)
    step = 1/np.sqrt(n)
    r = 0
    for i in range(1,n):
        coin_toss = 2*np.random.binomial(1,0.5)-1
        br[i] = r + step*coin_toss
        r = br[i]
    plt.plot(br)
    return br

