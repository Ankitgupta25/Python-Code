num= int (input("enter the number"))
s=0
temp=sum
while temp>0:
    c=temp % 10
    s+=c**3
    temp//=10
if num==s:
    print("armstrong number ")
else:
    print("not a armstrong number ")