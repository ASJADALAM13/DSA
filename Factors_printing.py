
num=int(input("Enter Your Number To get all the Factors of it:"))


#Brute force Method
def BF(num1):
    lst1=[]                   #S.C=O(k) ,where K=Total Number of Factors
    for i in range(1,num1+1):        #T.C=O(n)
        if num1%i==0:        #T.c of this Line=O(1))[will not taken into consideration]
            lst1.append(i)   #T.c of this Line=O(1))[will not taken into consideration]
    print(lst1)




#Better Solution
def BS(num2):
    lst2=[]                          #S.C=O(k) ,where K=Total Number of Factors
    for i in range(1,(num2//2)+1):   #T.C=O(n/2) almost equal to O(n)
        if num2%i==0:                #T.c of this Line=O(1)[will not taken into consideration]
            lst2.append(i)           #T.c of this Line=O(1))[will not taken into consideration]
    lst2.append(num2)
    print(lst2)


#optimal Solution
def OS(num3):
    lst3=[]                               #S,C=O(k)
    for i in range(1,(int(num3**0.5))+1): #T.C=O(root_n)
        if num3%i==0:
            lst3.append(i)
            if num3//i !=i:
                lst3.append(num3//i)
    print(lst3)

OS(num)