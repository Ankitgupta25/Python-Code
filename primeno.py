from numpy import number


number=int(input("Enter the Number:- "))
for i in range(2,number):
    if number%i==0:
        print("prime number")
        break
    else:
        print(" not a prime number")
        break