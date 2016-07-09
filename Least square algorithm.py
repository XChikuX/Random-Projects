import numpy as np
#import matplotlib.pyplot as plt
from math import *
Q=[]
def square(x):
	return pow(x,2)
D=[]
beacons=int(input("ENter no of beacons"))
bcx=[]
bcy=[]
#bcx beacon coordinate x
#bcy beacon coordinate y
#maybe filter with MAC adress later
for i in range(beacons):
	bcx.append(float(input("Enter X"+str(i))))
	bcy.append(float(input("Enter Y"+str(i))))
	D.append(3)   ############CHANGE THIS LATER
A=np.array([2*(bcx[beacons-1]-bcx[0]),2*(bcy[beacons-1]-bcy[0])])
print (A)
for i in range(1,beacons-1):
	O=np.array([2*(bcx[beacons-1]-bcx[i]),2*(bcy[beacons-1]-bcy[i])])
	A=np.concatenate((A,O))                                           #concatinating the remaining elements of A
	#print ("HEllo")
#A=np.array([2*(bcx[beacons-1]-bcx[0]),2*(bcy[beacons-1]-bcy[0]),2*(bcx[beacons-1]-bcx[1]),2*(bcy[beacons-1]-bcy[1]),2*(bcx[beacons-1]-bcx[2]),2*(bcy[beacons-1]-bcy[2])])
print (A)
B=A.reshape(beacons-1,2) #COnverts to a 2d array with beacons-1
for i in range(beacons-1):
	a=square(D[i])+square(bcx[beacons-1])+square(bcy[beacons-1])-(square(bcx[i])+square(bcy[i]))
	Q.append(a)
C=np.array(Q)

print (A)
print (B)

m, c = np.linalg.lstsq(B, C)[0]
print (m, c)
