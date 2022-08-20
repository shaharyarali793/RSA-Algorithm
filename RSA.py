#gcd function
#
def gcd(a,b):
    while True: 
        divisor = a%b
       # print(divisor)
        if (divisor ==0):
            return b
        else:
            a = b
            b = divisor
a= 8
b = 12
# print(gcd(a,b))


def RSA(p,q):
    #Public key 
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while(e<phi):

        if(gcd(e,phi)==1):
            break
        
        e = e+1


    #Private Key 
    #d = (1%phi)/e #Formula one
    k = 1
    d = (1 + (k*phi))/e
   


    #Message
    message = 7
    # Encryption c = (msg ^ e) % n
    c = (message**e)%n
   
    #Decryption m = (c ^ d) % n
    m = (c**d)%n
  

p = 11
q =3
RSA(p,q)
          
