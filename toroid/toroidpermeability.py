import math
import sys

#http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/indtor.html
print("Calculation of the Relative Permeability of the Toroid Core\n")
ans=input("Is the cross sectional area of the toroid round(1) or rectangular(2)?\n")

if ans==1:
    ans=input("Please input the diameter of the cross section in cm\n")/2*0.01 #radius cm to meters
    area=(math.pi)*(ans)(ans)
    print(area)
elif ans==2:    
    ans=input("Please input the height of the cross section in cm\n")*0.01#cm to meters
    area=ans
    ans=input("Please input the width the cross section in cm\n")*0.01#cm to meters
    area=area*ans
    print(area,'m2')
else :
    print("Undefined option, please input 1 or 2")
    sys.exit(1)

radius=input("Please input the diameter of the toroid, use the centerline\n")/2*0.01#cm to meters
N=input("Please input the number of coils\n")
L=input("Please input the inductance of the toroid inductor in mH\n")*0.001#mH to H


u=(2*math.pi*radius*L)/((N*N)*area)
ur=u/0.00000126 #1.26*10^-6, free space permeability
print("The Approximate Relative Permeability  of this Toroid is:\n")
print(ur)
