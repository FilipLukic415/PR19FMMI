import numpy as np
import matplotlib.pyplot as plt
from pyaxis import pyaxis
from collections import defaultdict

#Read the file
data = pyaxis.parse("H057S (1).px", encoding='windows-1250')
per_year_avto = defaultdict(int)
per_year_new = defaultdict(int)

for i in range(len(data["DATA"]["MERITVE"])):
    if data["DATA"]["MERITVE"][i] == "Število osebnih avtomobilov na dan 31. 12.":
        per_year_avto[data["DATA"]["LETO"][i]] += int(data["DATA"]["DATA"][i])
    if data["DATA"]["MERITVE"][i] == "Število prvih registracij novih osebnih avtomobilov":
        per_year_new[data["DATA"]["LETO"][i]] += int(data["DATA"]["DATA"][i])

years = []
num_of_avto = []
num_of_new = []

#Insert data into lists
for key in sorted(per_year_avto.keys()):
    years.append(int(key))
    num_of_avto.append(per_year_avto[key])

for key in sorted(per_year_new.keys()):
    num_of_new.append(per_year_new[key])

plt.figure()
#PLOT ALL VEHICLES DATA
plt.subplot(3, 1, 1)
plt.title("Število osebnih avtomobilov na dan - v letih 2004-2017")
plt.ylabel("Število avtomobilov")
plt.xlabel("Čas v letih")
plt.plot(years, num_of_avto)

#PLOT NEW VEHICLES DATA
plt.subplot(3, 1, 3)
plt.title("Število novo registriranih osebnih avtomobilov - v letih 2004-2017")
plt.ylabel("Število avtomobilov")
plt.xlabel("Čas v letih")
plt.plot(years, num_of_new)
plt.legend()
plt.show()
