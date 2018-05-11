#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

year,month,maxtp,mintp,mnmax,mnmin,rain = np.loadtxt('dublin-airport-monthly-nohead.csv', delimiter=',', usecols=(0,1,2,3,4,5,6), unpack=True)
wdsp,maxgt,sun = np.loadtxt('dublin-airport-monthly-nohead.csv', delimiter=',', usecols=(7,8,9), unpack=True)

def report_coldest_month():
    global mintp
    global month
    global year
    min_temp = np.amin(mintp)
    i = np.where(mintp==min_temp)
    print 'Coldest Month : Year: ',year[i],'  Month : ',month[i] , ' Temparature : ' , min_temp

def report_hottest_month():
    global maxtp
    global month
    global year
    max_temp = np.amax(maxtp)
    i = np.where(maxtp==max_temp)
    print 'Hottest Month : Year: ',year[i],'  Month : ',month[i] , ' Temparature : ' , max_temp

def show_mean_temparature():
    global maxtp
    global mintp
    global year
    meantp = (maxtp + mintp)/ 2
    plt.title("Dublin Airport - Mean Monthly Air Temperature 1985-2015")
    plt.xlabel("Year")
    plt.ylabel("Mean Temperature in Degrees Celcious")
    plt.plot(year,meantp ,c = 'b')
    plt.show()
    print np.split(meantp, 12)

def show_climate_change_indicators():
    global mintp
    global maxtp
    tp_less_zero = mintp[mintp < 0 ]
    tp_greater20 = maxtp[maxtp > 20 ]
    #print tp_less_zero
    #print tp_greater20
    plt.title("Dublin Airport - Mean Monthly Air Temperature 1985-2015 - WarmDays vs Frost Days")
    plt.ylabel("Temperature in Degrees Celcious")
    plt.bar(range(len(tp_less_zero)),tp_less_zero,color = 'b')
    plt.bar(range(len(tp_greater20)),tp_greater20,color = 'r')
    plt.show()


def show_yearly_temp():
    global month
    global maxtp
    global mintp
    month = month[0:12]
    maxtp1985 = maxtp[0:12]
    maxtp1986 = maxtp[12:24]
    mintp1985 = mintp[0:12]
    mintp1986 = mintp[12:24]
    plt.title("Dublin Airport - 1985 vs 1986")
    plt.ylabel("Temperature in Degrees Celcious")
    plt.xlabel("Month")
    plt.plot(month,maxtp1985 ,c = 'r')
    plt.plot(month,maxtp1986 ,c = 'r')
    plt.plot(month,mintp1985 ,c = 'b')
    plt.plot(month,mintp1986 ,c = 'b')
    plt.show()

if __name__ == "__main__":
    #report_coldest_month()
    #report_hottest_month()
    #show_mean_temparature()
    #show_climate_change_indicators()
    show_yearly_temp()
