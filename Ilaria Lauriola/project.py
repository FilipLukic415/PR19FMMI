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
i=data[:,7];
j=data[:,8];
k=data[:,9];
t=data[:,5];


%matplotlib inline
%config InlineBackend.figure_formats = ['jpg']
import matplotlib
import matplotlib.patches as mpatches
matplotlib.figure.Figure.__repr__ = lambda self: (
    f"<{self.__class__.__name__} size {self.bbox.size[0]:g}"
    f"x{self.bbox.size[1]:g} with {len(self.axes)} Axes>")

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


plt.figure(figsize=(8, 6))
p1 = plt.bar(y,x, color='red', align='center')
plt.ylabel('Number of fatal accidents')
plt.xlabel('Year')
plt.title('Road traffic fatal accidents')

plt.figure(figsize=(8, 6))
p2 = plt.bar(y,u, color='blue', align='center')
plt.ylabel('Number of person killed')
plt.xlabel('Year')
plt.title('Number of person killed in road traffic accidents')

plt.figure(figsize=(8, 6))
p3 = plt.bar(y,t, color='red', align='center')
plt.ylabel('Total Number of person involved')
plt.xlabel('Year')
plt.title('Number of person involved in road traffic accidents')

bar_width = 0.2;

plt.figure(figsize=(8, 6))
plt.bar(y,u, width=bar_width, color='green', zorder=2)
plt.bar(y + bar_width,i, width=bar_width, color='red', zorder=2)
plt.bar(y +bar_width*2,j, width=bar_width, color='orange', zorder=2)
plt.bar(y+bar_width*3,k, width=bar_width, color='blue', zorder=2)
plt.ylabel('Number of person involved in accidents, splitted by categories')
plt.xlabel('Year')

green_patch=mpatches.Patch(color='green',label='killed')
red_patch=mpatches.Patch(color='red',label='seriously injured')
orange_patch=mpatches.Patch(color='orange',label='slighty injured')
blue_patch=mpatches.Patch(color='blue',label='without injured')
plt.legend(handles=[green_patch,red_patch,orange_patch,blue_patch])
plt.show()