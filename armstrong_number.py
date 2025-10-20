#1.Brute Force Approach
num=int(input("Enter Number:"))
temp=num
rev=0
while num>0:
    nod=len(str(num))
    rev=rev+(num%10*10**(nod-1))
    num=num//10

print("original:",temp)
print("reversed:",rev)
print(temp==rev)