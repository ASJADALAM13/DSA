a="ASJAD"
b="AD"


i=0
j=len(b)
while i!=len(a):
    if a[i:j]==b:
        print(i,"is the first occurence  of the string")
        break
    i=i+1
    j=j+1

else:
    print(-1)
