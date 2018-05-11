#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def get_data():
    dates = np.genfromtxt('dublin-airport-daily-nohead.csv', usecols=(0), delimiter=',', dtype=None)
    maxtp, mintp = np.loadtxt('dublin-airport-daily-nohead.csv', delimiter=',', usecols=(2, 4), unpack=True)
    return dates, maxtp, mintp

if __name__ == "__main__":
    dates, maxtp, mintp = get_data()
    print "highest = ", np.max(maxtp)
    print "lowest  = ", np.min(maxtp)
    #plt.plot(maxtp, mintp)
    #plt.show()
