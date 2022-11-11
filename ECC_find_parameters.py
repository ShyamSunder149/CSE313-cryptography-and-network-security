from sage.all import *
# points p and q
ppoints = [,]
qpoints = [,]
#one parameter of elliptic curve
p = 
x2 = qpoints[0]
y2 = qpoints[1]
x1 = ppoints[0]
y1 = ppoints[1]
a = (y1**2-y2**2-x1**3+x2**3)*inverse(x1-x2,p)
b = y1**2-x1**3-a*x1
print(a,b)
