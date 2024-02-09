# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:56:26 2024

@author: Daniel
"""
import numpy as np
import matplotlib.pyplot as plt

def calcParametersEllipse(ecc,a,f):
    c = ecc * a
    h = f-c
    b = np.sqrt(a**2-c**2)
    
    return h,b

def getEllipse(ecc,a,k,f):
    theta = np.linspace(0, 2*np.pi,10000)
    
    h,b = calcParametersEllipse(ecc, a, f)
    xmin = h-a
    xmax = h+a
    x = (xmax-xmin)/2 * np.cos(theta) + h
    
    y = np.sqrt(b**2 * (1-(x-h)**2/a**2))
    
    for i in range(int(len(y)/2)):
        y[i] = -1 * y[i]
    
    return x,y+k

def calcParametersHyperbola(ecc,a,f):
    b = np.sqrt((ecc**2 - 1) * a**2)
    c = np.sqrt(a**2 + b**2)
    h = f + c
    
    return h,b

def getHyperbola(ecc,a,k,f):
    h,b = calcParametersHyperbola(ecc, a, f)
    
    y = np.linspace(-2,2,1000)
    
    x = -1 * np.sqrt(a**2 * (1+(y-k)**2/b**2)) + h
    
    return x,y

def getPeriAndApo(x,y,ecc):
    if ecc > 1:
        apo = np.inf
        absY = np.abs(y)
        index  = min(range(len(absY)), key=absY.__getitem__)
        
        peri = abs(x[index])
    
    else:
        minYIndexes = []
        extremeXValues = []
        for j in range(len(y)):
            if abs(y[j]) < .001:
                minYIndexes.append(j)
        for j in range(len(minYIndexes)):
            extremeXValues.append(x[minYIndexes[j]])
        
        apo = np.max(np.abs(extremeXValues))
        peri = np.min(np.abs(extremeXValues))
    
    return peri,apo

def main(ecc=0, a=1, k=0,f=0):
    eccList = np.linspace(0,2,150)
    i = 0
    for ecc in eccList:
        if ecc < 1:
            x,y = getEllipse(ecc, a, k, f)
            peri,apo = getPeriAndApo(x,y,ecc)
            semi = peri + apo
        
        if ecc > 1:
            x,y = getHyperbola(ecc, a, k, f)
            peri,apo = getPeriAndApo(x,y,ecc)
            semi = np.nan
            
        fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
        ax.plot(x,y,color='black',linewidth=4)
        ax.plot(0,0,marker='*',ms=20,color='gold')
        ax.set_aspect('equal')
        ax.set_xlim([-2,2])
        ax.set_ylim([-2,2])
        ax.tick_params(axis='both', which='major', labelsize=20)
        ax.tick_params(axis='both', which='minor', labelsize=15)
        
        text = 'Eccentricity: '+ str(round(ecc,2)) + '\n' + 'Semi-Major Axis: ' + str(round(semi,3)) + '\n' + 'Periapsis: ' + str(round(peri,3)) + '\n' + 'Apoapsis: ' + str(round(apo,3))
        
        ax.text(.77,1.5,text,size=7)
        imageName = 'kepler_first_' + str(i) + '.png'
     
        fig.savefig('D:/Graduate_Research/Animated_gif_library/gifs_chapter/chapter_3/keplers_first/keplers_first_images/' + imageName,bbox_inches='tight',dpi=300)   # save the figure to file
        plt.close(fig)
        
        i = i + 1
    
    
    