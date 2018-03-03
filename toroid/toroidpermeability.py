import math
#http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/indtor.html
print("Calculation of the Relative Permeability of the Toroid Core\n")
ans=input("Is the cross sectional area of the toroid round(1) or rectangular(2)?\n")
print(ans,type(ans))

if ans==1:
    ans=input("Please input the diameter of the cross section in cm\n")
    area=(math.pi)*(ans/2)*0.01*(ans/2)*0.01#cm to meters
    print(area)
else:    
    ans=input("Please input the height of the cross section in cm\n")
    area=ans*0.01#cm to meters
    ans=input("Please input the width the cross section in cm\n")
    area=area*ans*0.01 #cm to meters
    print(area,'m2')

ans=input("Please input the diameter of the toroid, use the centerline\n")
radius=(ans/2)*0.01#cm to meters
ans=input("Please input the number of coils\n")
N=ans

ans=input("Please input the inductance of the toroid inductor in mH\n")
L=ans*0.001#mH to H

u=(2*math.pi*radius*L)/((N*N)*area)
ur=u/0.00000126 #1.26*10^-6, free space permeability
print("The Approximate Relative Permeability  of this Toroid is:\n")
print(ur)
