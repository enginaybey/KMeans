"""
@author: engin aybey

topic: k-means
"""
import matplotlib.pyplot as plt
import numpy as np
from random import uniform
x=[]
y=[]
coor=[]
filename = "data.txt"
file = open(filename, "r")
for line in file:
    tmp=line.split()
    print(tmp)
    x.append(float(tmp[0]))
    y.append(float(tmp[1]))
    coor.append([float(tmp[0]),float(tmp[1])])
file.close()
plt.plot(x,y,'ro')
plt.axis([0, 10, 0, 10])
k1=[0,0]
k2=[0,0]

k1[0]=uniform(0, 10)
k1[1]=uniform(0, 10)
k2[0]=uniform(0, 10)
k2[1]=uniform(0, 10)
print(k1,k2)
l1=[]
l2=[]
tmp1=[100.0,100.0]
tmp2=[100.0,100.0]
plt.plot(k1[0],k1[1],'bs')
plt.plot(k2[0],k2[1],'g^')
plt.show()
def distance(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**(0.5)
count=0
while True:
    l1=[]
    l2=[]
    for i in range(len(coor)):
        d1=distance(coor[i],k1)
        d2=distance(coor[i],k2)
        
        if d1<d2:
            l1.append(coor[i])
        else:
            l2.append(coor[i])
    
    if len(l1)!=0:
        k1[0]= np.mean([l[0] for l in l1])
        k1[1]= np.mean([l[1] for l in l1])
    else:
        k1[0]=uniform(k1[0], 10)
        k1[1]=uniform(k1[1], 10)
    if len(l2)!=0:
        k2[0]= np.mean([l[0] for l in l2])
        k2[1]= np.mean([l[1] for l in l2])
    else:
        k2[0]=uniform(k2[0], 10)
        k2[1]=uniform(k2[1], 10)
    count+=1
    if distance(k1,tmp1)==0 and distance(k2,tmp2)==0: break
    tmp1=k1[:]
    tmp2=k2[:]
if len(l1)!=0: print(l1)
if len(l2)!=0: print(l2)
print("\nNumber of iteration:", count)
if len(l1)!=0: plt.plot([l[0] for l in l1],[l[1] for l in l1],'yo')
if len(l2)!=0: plt.plot([l[0] for l in l2],[l[1] for l in l2],'co')
plt.plot(k1[0],k1[1],'bs')
plt.plot(k2[0],k2[1],'g^')
plt.axis([0, 10, 0, 10])
plt.show()
sum1=0
sum2=0
filename = "output.txt"
file = open(filename, "w")
file.writelines("1.cluster\n")
for l in l1:
    file.writelines("%.2f %.2f\n" %(l[0] ,l[1]))
file.writelines("1.center\n")
file.writelines("%.2f %.2f\n" %(k1[0] ,k1[1]))
file.writelines("==========================================\n")
file.writelines("2.cluster\n")
for l in l2:
    file.writelines("%.2f %.2f\n" %(l[0] ,l[1]))
file.writelines("2.center\n")
file.writelines("%.2f %.2f\n" %(k2[0] ,k2[1]))
for l in l1:
    sum1+=distance(k1,l)
for l in l2:
    sum2+=distance(k2,l)
file.writelines("==========================================\n")
file.writelines("Summation of the distances of 1.cluster points from 1.center\n")
file.writelines("%.5f \n" %sum1)
file.writelines("Summation of the distances of 2.cluster points from 2.center\n")
file.writelines("%.5f \n" %sum2)
file.close()
#print(sum1,sum2)