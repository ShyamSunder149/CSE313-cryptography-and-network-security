def fun(a,b):
        if a%b == 0:
                return b
        else:
                return fun(b,a%b)

def main():
        x,y = int(input("enter 2 numbers"))
        print(fun(x,y))

main()
