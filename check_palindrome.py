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






