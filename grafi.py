# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:39:33 2021

@author: gaspe
"""

import matplotlib.pyplot as plt

labels = 'AC-130', 'B52', 'Pilatus'
sizes = [60.8,39,0.2]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Relacija Ljubljana - Boston')
plt.show()