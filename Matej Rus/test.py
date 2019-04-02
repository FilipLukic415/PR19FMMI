from pyaxis import pyaxis
from collections import defaultdict

import matplotlib.pyplot as plt

# read table from file
px = pyaxis.parse("2222003S.PX", encoding='windows-1250')


# save all the accidents per year
# dictionary = {key: year, value: number of accidents}
accidents_per_year = defaultdict(int)

for x in range(len(px["DATA"]["MERITVE"])):
    if px["DATA"]["MERITVE"][x] == "Prometne nesreče - SKUPAJ":
        accidents_per_year[px["DATA"]["LETO"][x]] += int(px["DATA"]["DATA"][x])



# lists for plotting
years = []
num_of_accidents = []

# fill lists with data for plotting
for key in sorted(accidents_per_year.keys()):
    years.append(int(key))
    num_of_accidents.append(accidents_per_year[key])

# name the axis
plt.title("Number of accidents for each year 2003 - 2014")
plt.ylabel("Number of accidents")
plt.xlabel("Time in years")

# plot the data
plt.plot(years, num_of_accidents)
plt.show()
'''

# {key: year, value: {key: month, value: percentage_of_accitends_for_this_year}}
d = defaultdict(lambda: defaultdict(float))

# calculate the percentage of accidents for months for each year
for x in range(len(px["DATA"]["MERITVE"])):
    if px["DATA"]["MERITVE"][x] == "Prometne nesreče - SKUPAJ":
        d[ int(px["DATA"]["LETO"][x]) ][ px["DATA"]["MESEC NESREČE"][x] ] = float(px["DATA"]["DATA"][x]) / accidents_per_year[px["DATA"]["LETO"][x]]


# {key: month, value: percentage}
dm = defaultdict(float)
# sum all the percentages for the same months
for year in d.keys():
    for month in d[year].keys():
        dm[month] += d[year][month]

months = []
percentages = []

# divide all percentage sum by number of years and make tables for plot display
for month in dm.keys():
    months.append(month[:3])
    percentages.append((dm[month] / 12))

plt.xlabel("Months")
plt.ylabel("Percentage of accidents")
plt.title("Percentage of accidents from 2003 to 2014")
plt.bar(months, percentages, align="center")
plt.show()

'''