#1.Brute Force Approach
n1=18
n2=24
x=min(n1,n2)
for i in range(x//2,2,-1):
    if n1%i==0 and n2%i==0:
        print(f"GCD of {n1},{n2} is:{i}")
        break
else:
    print("False")
