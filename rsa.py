from Crypto.Util.number import inverse
from math import gcd
p = 11
q = 17
m = 22
phi = (p-1)*(q-1)
n = p*q 
for i in range(2,n): 
    if gcd(i,phi) == 1:
        e = i
        break
print(e)
d = inverse(e,phi)
ct = pow(m,e,n)
pt = pow(ct,d,n)
print(ct)
print(pt)