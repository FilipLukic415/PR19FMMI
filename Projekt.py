

steviloNesrecAC = [2009,2409,1696,1851,1757,1519,1503,2290,2077,2052,2040,1820]
steviloNesrecVNaselju = [26217,27300,19469,20167,20014,14968,13602,14015,15675,14922,12725,12402]
steviloNesrecIzvenNaselja = [12944,13295,9929,9551,8630,6296,5492,5042,	5161,5061,4139,4029]

import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 12

"""
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, steviloNesrecAC, bar_width,
                 alpha=opacity,
                 color='b',
                 label='AC')

rects2 = plt.bar(index + bar_width, steviloNesrecVNaselju, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Naselje')

rects3 = plt.bar(index +  bar_width + bar_width, steviloNesrecIzvenNaselja, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Izven')

plt.xlabel('Leta')
plt.ylabel('Stevilo nesrec')


plt.xticks(index + bar_width, ('2003', '2004', '2005', '2006','2007', '2008', '2009', '2010','2011','2012', '2013', '2014'))
plt.legend()

plt.tight_layout()
plt.show()

"""


######
"""
# set width of bar
barWidth = 0.25

# set height of bar
bars1 = steviloNesrecAC
bars2 = steviloNesrecVNaselju
bars3 = steviloNesrecIzvenNaselja

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, bars1, color='red', width=barWidth, edgecolor='white', label='število nesreč na AC')
plt.bar(r2, bars2, color='blue', width=barWidth, edgecolor='white', label='število nesreč v naselju')
plt.bar(r3, bars3, color='green', width=barWidth, edgecolor='white', label='število nesreč izven naselju')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['2003', '2004', '2005', '2006','2007', '2008', '2009', '2010','2011','2012', '2013', '2014'])
plt.xlabel('Leta',fontweight='bold')
plt.ylabel('Število nesreč',fontweight='bold')
# Create legend & Show graphic
plt.title("Prikaz števila nesreč glede na lokacijo",fontweight='bold')
plt.legend()
plt.show()
#######
#mrtvi po letih

seznamLet = [2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
steviloMrtvih = [220,254,230,233,263,200,154,127,129,122,116,97]

"""


# set width of bar
plt.title("Prikaz števila poškodovanih",fontweight='bold')
plt.legend()

barWidth = 0.5
steviloRanjenih = [11640,9165,8717,7659,7257,6857,6568,6345,6578,6495]
# set height of bar
bars1 = steviloRanjenih
r1 = np.arange(len(bars1))
plt.bar(r1, bars1, color='red', width=barWidth, label='število ranjenih')
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth -0.50 for r in range(len(bars1))], ['2007', '2008', '2009', '2010','2011', '2012', '2013', '2014','2015','2016'])
plt.xlabel('Leta',fontweight='bold')
plt.ylabel('Število poškodovanih',fontweight='bold')
plt.show()


# set width of bar
plt.title("Prikaz števila poškodovanih",fontweight='bold')
plt.legend()

barWidth = 0.25
steviloRanjenih = [11640,9165,8717,7659,7257,6857,6568,6345,6578,6495]
# set height of bar
bars1 = steviloRanjenih
r1 = np.arange(len(bars1))
plt.bar(r1, bars1, color='red', width=barWidth, edgecolor='green', label='število ranjenih')
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['2007', '2008', '2009', '2010','2011', '2012', '2013', '2014','2015','2016'])
plt.xlabel('Leta',fontweight='bold')
plt.ylabel('Število ranjenih',fontweight='bold')
plt.show()


"""
female = [59,36,39,34,28,33,31,30,30,28]
male = [232,178,132,104,113,97,94,78,90,102]
years = ['2007', '2008', '2009', '2010','2011', '2012', '2013', '2014','2015','2016']



x = years
# create an index for each tick position
xi = [i for i in range(0, len(x))]
y = male
y2 = female
plt.ylim(0,400)
# plot the index for the x-values
plt.plot(xi, y,  color='b', label='Moški')
plt.plot(xi, y2, color='r', label='Ženske')
plt.ylabel("Število poškodovanih")
plt.xlabel("Leta")
plt.xticks(xi, x)
plt.title("Razmerje poškodovanih po letih za moški/ženske ")
plt.legend()
plt.show()
"""
