x=int(input("Enter no:"))
'''

def check_palindrome(num):
    n=num
    pald=0
    while n!=0:
        ld=n%10
        pald=(pald*10)+ld
        n=n//10

    if num==pald:
        print("Palindrome")
    else:
        print("Not A palindrome")

check_palindrome(num)
'''



if x<0 or(x!=0 and x%10==0):
    print(False)
if x==0:
    print(True)

y=0




