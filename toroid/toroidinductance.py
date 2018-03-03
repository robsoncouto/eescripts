import math
import sys
#http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/indtor.html
print("Calculation of the Approximate Inductance of a Toroid\n")
ans=int(input("Is the cross sectional area of the toroid round(1) or rectangular(2)?\n"))

if ans==1:
    ans=float(input("Please input the diameter of the cross section in cm\n"))/2*0.01 #radius cm to meters
    area=(math.pi)*(ans)(ans)
    print(area)
elif ans==2:    
    ans=float(input("Please input the height of the cross section in cm\n"))*0.01#cm to meters
    area=ans
    ans=float(input("Please input the width the cross section in cm\n"))*0.01#cm to meters
    area=area*ans
    print("Area: {:f}m2".format(area))
else :
    print("Undefined option, please input 1 or 2")
    sys.exit(1)

radius=float(input("Please input the diameter of the toroid, use the centerline\n"))/2*0.01#cm to meters
N=int(input("Please input the number of coils\n"))

ur=float(input("Please input Relative permeability of the core.\n"))
u=ur*0.00000126

L=(u*(N*N)*area)/(2*math.pi*radius)
print("The Approximate Inductance of this Toroid is:\n")
print(L)
