import math
#http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/indtor.html
print("Calculation of the Approximate Inductance of a Toroid\n")
ans=input("Is the cross sectional area of the toroid round(1) or rectangular(2)?\n")
print(ans,type(ans))

if ans==1:
    ans=input("Please input the diameter of the cross section in cm\n")
    area=(2*math.pi)*(ans/2)
    print(area)
else:    
    ans=input("Please input the height of the cross section in cm\n")
    area=ans
    ans=input("Please input the width the cross section in cm\n")
    area=area*area
    print(area)

ans=input("Please input the diameter of the toroid, use the centerline\n")
radius=ans/2
ans=input("Please input the number of coils\n")
N=ans/2

ans=input("Please input Relative permeability of the core.\n")
u=ans/2

L=(u*(N*N)*area)/(2*math.pi*radius)
print("The Approximate Inductance of this Toroid is:\n")
print(L)
