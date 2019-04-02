# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:57:04 2019

@author: ilala
"""
import numpy as np
from numpy import genfromtxt
data = genfromtxt('accidents.csv', delimiter=';',skip_header=1)

y=data[:,0]; #years
x=data[:,2]; #fatal accidents
u=data[:,6]; #people killed



%matplotlib inline
%config InlineBackend.figure_formats = ['jpg']
import matplotlib
matplotlib.figure.Figure.__repr__ = lambda self: (
    f"<{self.__class__.__name__} size {self.bbox.size[0]:g}"
    f"x{self.bbox.size[1]:g} with {len(self.axes)} Axes>")

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


plt.figure()
p1 = plt.bar(y,x, color='red', align='center')
plt.ylabel('Number of fatal accidents')
plt.xlabel('Year')
plt.title('Road traffic fatal accidents')

plt.figure()
p2 = plt.bar(y,u, color='blue', align='center')
plt.ylabel('Number of person killed')
plt.xlabel('Year')
plt.title('Number of person killed in road traffic accidents')






