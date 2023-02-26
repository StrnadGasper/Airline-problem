# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:16:31 2021

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
poti = np.array([225,225,420,420,300,300,225,225,420,420,300,300])
povp = np.array([4000,6200,3750,4700,5150,6000,4000,6200,3750,4700,5150,6000])
hitrosti = np.array([50,50,50,50,50,50,60,60,60,60,60,60])
casleta= poti/hitrosti
stzicov = np.array([45,45,45,45,45,45,80,80,80,80,80,80])
minstzic = stzicov*-1
stroskleta = np.array([2000,2000,2000,2000,2000,2000,4200,4200,4200,4200,4200,4200])
cenakarte =np.array([210,210,390,390,270,270,200,200,390,390,270,270])
profitenlet= stzicov*cenakarte-stroskleta*casleta
print(profitenlet)
minpel = profitenlet*-1
ljbos1 = np.array([45,0,0,0,0,0,0,0,0,0,0,0])*-1
boslj1= np.array([0,45,0,0,0,0,0,0,0,0,0,0])*-1
ljse1= np.array([0,0,45,0,0,0,0,0,0,0,0,0])*-1
selj1= np.array([0,0,0,45,0,0,0,0,0,0,0,0])*-1
ljjo1= np.array([0,0,0,0,45,0,0,0,0,0,0,0])*-1
jolj1= np.array([0,0,0,0,0,45,0,0,0,0,0,0])*-1
ljbos2= np.array([0,0,0,0,0,80,0,0,0,0,0,0])*-1
boslj2= np.array([0,0,0,0,0,0,0,80,0,0,0,0])*-1
ljse2= np.array([0,0,0,0,0,0,0,0,80,0,0,0])*-1
selj2= np.array([0,0,0,0,0,0,0,0,0,80,0,0])*-1
ljjo2= np.array([0,0,0,0,0,0,0,0,0,0,80,0])*-1
jolj2= np.array([0,0,0,0,0,0,0,0,0,0,0,80])*-1

# c je una stvar ko jo gledam
c = profitenlet*-1

utezi = np.array([minstzic,stzicov,ljbos1,boslj1,ljse1,selj1,ljjo1,jolj1,
ljbos2,boslj2,ljse2,selj2,ljjo2,jolj2])
meje =np.array([-59000, 63000,4000*-1,6200*-1,3750*-1,4700*-1,5150*-1,6000*-1,4000*-1,6200*-1,3750*-1,4700*-1,5150*-1,6000*-1])
zacetek = time.time()
l = linprog(c, A_ub = utezi, b_ub = meje, bounds = [(0,None),(0,None),(0,700),(0,700),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None)])
print('Optimal value:', round(l.fun, ndigits=2),
      '\nx values:', l.x,
      '\nNumber of iterations performed:', l.nit,
      '\nStatus:', l.message)
konec = time.time()
print('Čas trajanja funkcije:')
print(konec-zacetek)
data = {'LJ-BOS':89,'BOS-LJ':138,'LJ-SE':83,'SE-LJ':104,'LJ-JOH':114,'JOH-LJ':133,}
leti = list(data.keys())
stevilo = list(data.values())
fig = plt.figure(figsize = (10,5))
plt.bar(leti,stevilo,color = 'maroon',width = 0.3)
plt.xlabel('Relacija')
plt.ylabel('Število letov')
plt.title('Letalo AC-130 (45 sedežev)')
plt.show()

data = {'LJ-BOS':0,'BOS-LJ':78,'LJ-SE':93,'SE-LJ':105,'LJ-JOH':64,'JOH-LJ':75,}
leti = list(data.keys())
stevilo = list(data.values())
fig = plt.figure(figsize = (10,5))
plt.bar(leti,stevilo,color = 'maroon',width = 0.3)
plt.xlabel('Relacija')
plt.ylabel('Število letov')
plt.title('Letalo B52 (80 sedežev)')
plt.show()


poleti = np.array([89,138,83,104,114,133,0,78,93,105,64,75])
ure = poleti*casleta
print(ure)
print(np.sum(ure))

print(739625/6448)