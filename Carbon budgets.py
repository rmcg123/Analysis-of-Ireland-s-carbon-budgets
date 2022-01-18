# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:44:52 2022

@author: MCGUINRO
"""
import numpy as np
import matplotlib.pyplot as plt


enwi18=37+3.2+1
aflu18=22.3+4.8

tot18=enwi18+aflu18

x=np.linspace(0.20,0.60,40)
y=-enwi18/aflu18 *x +0.49*(tot18/aflu18)

plt.plot(x,y)
plt.xlabel("% change in energy, \n industry and waste emissions")
plt.ylabel("% change in agriculture, \n forestry and land-use emissions")
plt.title("Trade-off between emissions reductions in the \n energy system and agriculture and land-use sectors")
plt.xticks(np.linspace(0.2,0.6,5),100*np.linspace(0.8,0.4,5))
plt.yticks(np.linspace(0.3,0.9,7),100*np.linspace(0.7,0.1,7))
plt.grid()
plt.show()

reds=[]
for i in range(100000):
    reds.append(np.random.uniform(0.9,1.02,9))
    
finalred=[]
for i in range(100000):
    finalred.append(0.49/np.prod(reds[i]))

allreds=[]
for i in range(100000):
    if finalred[i]<0.9 or finalred[i]>1.02:
        []
    else:
        allreds.append(np.append(reds[i],finalred[i]))

## Randomly ordered

cums=[]
for i in range(len(allreds)):
    for j in range(1,11,1):
        cums.append(np.prod(allreds[i][0:j])*tot18)
        
buds1=[]
for i in range(len(allreds)):
        buds1.append(sum(cums[0+10*i:5+10*i]))
        
plt.hist(buds1,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("First carbon budget")
plt.show()
        
buds2=[]
for i in range(len(allreds)):
        buds2.append(sum(cums[5+10*i:10+10*i]))
        
plt.hist(buds2,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Second carbon budget")
plt.show()

totalcbs=[]
for i in range(len(allreds)):
        totalcbs.append(sum(cums[0+10*i:10+10*i]))
        
plt.hist(totalcbs,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Carbon budget over decade")
plt.show()
        
## Backloaded
        
blreds=[]
for i in range(len(allreds)):
    blreds.append(sorted(allreds[i],reverse=True))
    
blcums=[]
for i in range(len(allreds)):
    for j in range(1,11,1):
        blcums.append(np.prod(blreds[i][0:j])*tot18)
        
blbuds1=[]
for i in range(len(allreds)):
        blbuds1.append(sum(blcums[0+10*i:5+10*i]))
        
plt.hist(blbuds1,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("First carbon budget (backloaded)")
plt.show()
        
blbuds2=[]
for i in range(len(allreds)):
        blbuds2.append(sum(blcums[5+10*i:10+10*i]))
        
plt.hist(blbuds2,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Second carbon budget (backloaded)")
plt.show()

totalblcbs=[]
for i in range(len(allreds)):
        totalblcbs.append(sum(blcums[0+10*i:10+10*i]))
        
plt.hist(totalblcbs,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Carbon budget over decade (backloaded)")
plt.show()

## Frontloaded
        
flreds=[]
for i in range(len(allreds)):
    flreds.append(sorted(allreds[i]))
    
flcums=[]
for i in range(len(allreds)):
    for j in range(1,11,1):
        flcums.append(np.prod(flreds[i][0:j])*tot18)
        
flbuds1=[]
for i in range(len(allreds)):
        flbuds1.append(sum(flcums[0+10*i:5+10*i]))
        
plt.hist(flbuds1,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("First carbon budget (frontloaded)")
plt.show()
        
flbuds2=[]
for i in range(len(allreds)):
        flbuds2.append(sum(flcums[5+10*i:10+10*i]))
        
plt.hist(flbuds2,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Second carbon budget (frontloaded)")
plt.show()

totalflcbs=[]
for i in range(len(allreds)):
        totalflcbs.append(sum(flcums[0+10*i:10+10*i]))
        
plt.hist(totalflcbs,density=True)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Carbon budget over decade (frontloaded)")
plt.show()

## Comparison

plt.hist(buds1,density=True,alpha=0.6)
plt.hist(blbuds1,density=True,alpha=0.6)
plt.hist(flbuds1,density=True,alpha=0.6)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Comparison of pathways for first carbon budget")
plt.legend(["random","backloaded","frontloaded"])
plt.show()

plt.hist(buds2,density=True,alpha=0.6)
plt.hist(blbuds2,density=True,alpha=0.6)
plt.hist(flbuds2,density=True,alpha=0.6)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Comparison of pathways for second carbon budget")
plt.legend(["random","backloaded","frontloaded"])
plt.show()


plt.hist(totalcbs,density=True,alpha=0.6)
plt.hist(totalblcbs,density=True,alpha=0.6)
plt.hist(totalflcbs,density=True,alpha=0.6)
plt.xlabel("MtCO2eq")
plt.ylabel("Probability density")
plt.title("Comparison of pathways for decade")
plt.legend(["random","backloaded","frontloaded"])
plt.show()