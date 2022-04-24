def egcd(a,b):
	if a == 0:
		return b,0,1
	else:
		gcd,x,y = egcd(b%a,a)
		return gcd, y - (b//a)*x,x

def main():
	a,b = int(input('enter 2 numbers:'))

main()
