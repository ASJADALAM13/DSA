
#Function To Find The Remainder Of Num Divided By Divisor
def mod(Divisor,Num):
    print (Num-(Divisor * (Num//Divisor)))

#mod(8,93)



#Function To find GCD of two Numbers
def GCD(n,m):
    rem=1 
    while rem!=0:
        rem=n%m 
        n=m 
        m=rem 

    return n #as GCD

#Function To Find LCM of Two Numbers Using GCD Method
def LCM(n,m):
    return (n*m)/GCD(n,m) #as LCM

g=GCD(10,15)
print(g)

l=LCM(10,15)
print(l)