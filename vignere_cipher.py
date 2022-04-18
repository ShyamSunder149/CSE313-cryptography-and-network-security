from string import ascii_lowercase
from itertools import cycle,islice

x = list(ascii_lowercase)

def encrypt():
        s = input("enter plaintext")
        s1 = input("Enter key")
        s2 = ''
        key = ''.join(islice(cycle(s1),len(s)))
        for i,j in zip(s,key):
                s2 += x[(x.index(i)+x.index(j))%26]
        print("Ciphertext:",s2)

def decrypt():
        s = input("enter ciphertext")
        s1 = input("Enter key")
        s2 = ''
        key = ''.join(islice(cycle(s1),len(s)))
        for i,j in zip(s,key):
                s2+= x[(x.index(i)-x.index(j))%26]
        print("Plaintext:",s2)

def main():
        while(True):
                n = int(input('Enter your choice:\n[1]Encrypt\n[2]Decrypt\n[3]Exit'))
                if n == 1:
                        encrypt()
                elif n == 2:
                        decrypt()
                else:
                        exit()

main()
