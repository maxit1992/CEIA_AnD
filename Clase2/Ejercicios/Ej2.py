# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:26:53 2021

@author: MaxiT
"""

import numpy as np
import matplotlib.pyplot as plt

curtosis=0
IQR=0
s_muestreal=0
skewness=0

for i in range(0,1000):

    values=np.random.exponential(1,100)
    
    curtosis=curtosis+ 1/1000*np.sum(np.power((values-1)/1,4))/100
    
    skewness=skewness+ 1/1000*np.sum(np.power((values-1)/1,3))/100
    
    
    
    IQR= IQR+ 1/1000* (np.percentile(values,75) - np.percentile(values,25))
    
    s_muestreal= s_muestreal + 1/1000 * \
        (np.percentile(values,97.5) - np.percentile(values,2.5)) / 4

plt.boxplot(values)

print("Curtosis {}".format(curtosis))
print("Skewness {}".format(skewness))
print("IQR {}".format(IQR))
print("Desvío muestreal {}".format(s_muestreal))

