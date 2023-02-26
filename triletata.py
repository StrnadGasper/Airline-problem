# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:53:41 2021

@author: gaspe
"""

import time
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# koeficienti so po 12 za vsak razl avion in razlino pot iz lj v 1,3,4 in kontra
poti = np.array([225,225,420,420,300,300,225,225,420,420,300,300,225,225,420,420,300,300])
povp = np.array([4000,6200,3750,4700,5150,6000,4000,6200,3750,4700,5150,6000,4000,6200,3750,4700,5150,6000])
hitrosti = np.array([50,50,50,50,50,50,60,60,60,60,60,60,90,90,90,90,90,90])
casleta= poti/hitrosti
stzicov = np.array([45,45,45,45,45,45,80,80,80,80,80,80,20,20,20,20,20,20])
minstzic = stzicov*-1
stroskleta = np.array([2000,2000,2000,2000,2000,2000,4200,4200,4200,4200,4200,4200,5000,5000,5000,5000,5000,5000])
cenakarte =np.array([210,210,390,390,270,270,200,200,390,390,270,270,660,660,1200,1200,850,850])
profitenlet= stzicov*cenakarte-stroskleta*casleta
print(profitenlet)

minpel = profitenlet*-1
ljbos1 = np.array([45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])*-1
boslj1= np.array([0,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])*-1
ljse1= np.array([0,0,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])*-1
selj1= np.array([0,0,0,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0])*-1
ljjo1= np.array([0,0,0,0,45,0,0,0,0,0,0,0,0,0,0,0,0,0])*-1
jolj1= np.array([0,0,0,0,0,45,0,0,0,0,0,0,0,0,0,0,0,0])*-1
ljbos2= np.array([0,0,0,0,0,80,0,0,0,0,0,0,0,0,0,0,0,0])*-1
boslj2= np.array([0,0,0,0,0,0,0,80,0,0,0,0,0,0,0,0,0,0])*-1
ljse2= np.array([0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,0,0,0])*-1
selj2= np.array([0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,0,0])*-1
ljjo2= np.array([0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0,0])*-1
jolj2= np.array([0,0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0,0])*-1
ljbos3 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0,0,0])*-1
boslj3= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0,0])*-1
ljse3 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0])*-1
selj3= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0])*-1
ljjo3= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,0])*-1
jolj3= np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20])*-1
# c je una stvar ko jo gledam
c = profitenlet*-1

utezi = np.array([minstzic,stzicov,ljbos1,boslj1,ljse1,selj1,ljjo1,jolj1,
ljbos2,boslj2,ljse2,selj2,ljjo2,jolj2,ljbos2,boslj2,ljse2,selj3,ljjo3,jolj3])
meje =np.array([-59000, 63000,4000*-1,6200*-1,3750*-1,4700*-1,5150*-1,6000*-1,4000*-1,6200*-1,3750*-1,4700*-1,5150*-1,6000*-1,4000*-1,6200*-1,3750*-1,4700*-1,5150*-1,6000*-1])
zacetek = time.time()
l = linprog(c, A_ub = utezi, b_ub = meje)
print('Optimal value:', round(l.fun, ndigits=2),
      '\nx values:', l.x,
      '\nNumber of iterations performed:', l.nit,
      '\nStatus:', l.message)
konec = time.time()
print('Čas trajanja funkcije:')
print(konec-zacetek)
data = {'LJ-BOS':87,'BOS-LJ':139,'LJ-SE':85,'SE-LJ':106,'LJ-JOH':115,'JOH-LJ':134,}
leti = list(data.keys())
stevilo = list(data.values())
fig = plt.figure(figsize = (10,5))
plt.bar(leti,stevilo,color = 'maroon',width = 0.3)
plt.xlabel('Relacija')
plt.ylabel('Število letov')
plt.title('Letalo AC-130 (45 sedežev)')
plt.show()

data = {'LJ-BOS':1,'BOS-LJ':79,'LJ-SE':47,'SE-LJ':60,'LJ-JOH':65,'JOH-LJ':76,}
leti = list(data.keys())
stevilo = list(data.values())
fig = plt.figure(figsize = (10,5))
plt.bar(leti,stevilo,color = 'maroon',width = 0.3)
plt.xlabel('Relacija')
plt.ylabel('Število letov')
plt.title('Letalo B52 (80 sedežev)')
plt.show()

data = {'LJ-BOS':1,'BOS-LJ':1,'LJ-SE':3,'SE-LJ':238,'LJ-JOH':260,'JOH-LJ':302,}
leti = list(data.keys())
stevilo = list(data.values())
fig = plt.figure(figsize = (10,5))
plt.bar(leti,stevilo,color = 'maroon',width = 0.3)
plt.xlabel('Relacija')
plt.ylabel('Število letov')
plt.title('Letalo Pilatus (20 sedežev)')
plt.show()

poleti = np.array([87,139,85,106,115,134,1,79,47,60,65,76,1,1,3,238,260,302])
urelet = poleti *casleta
print(sum(urelet))

print(927972/sum(urelet))