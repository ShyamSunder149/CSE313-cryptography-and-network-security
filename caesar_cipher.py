from string import ascii_lowercase

x = list(ascii_lowercase)

def encrypt():
        s = input('enter plaintext')
        s1 = int(input('enter shift'))
        s2 = ''
        for i in s:
                s2 += x[(x.index(i)+s1)%26]
        print('Ciphertext:',s2)

def decrypt():
        s = input('enter ciphertext')
        s1 = int(input('enter shift'))
        s2 = ''
        for i in s:
                s2 += x[(x.index(i)-s1)%26]
        print('Ciphertext:',s2)

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
