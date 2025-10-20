'''num=int(input("Enter:"))
rev=0
while num>0:
    nod=len(str(num))
    rev=rev+(num%10)*(10**(nod-1))
    num=num//10
print(rev)
'''


rev=0
