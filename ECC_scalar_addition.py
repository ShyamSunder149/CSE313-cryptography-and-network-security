from sage.all import *
points = [,] #provide points here
#elliptic curve parameters
p = 
a = 
b = 
u =   #Scalar which needs to get multiplied
E = EllipticCurve(GF(p),[a,b])
ans = E(points[0],points[1])*u
print(ans)
