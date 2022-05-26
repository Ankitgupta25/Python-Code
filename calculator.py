from re import T


def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b
def si (p,r,t):
    return (p*r*t)/100
def ci (p,r,t):
    return p*pow((1+r/100),T)
def sqr(num):
    return num**2
def srt (num):
    return num**0.5

print(si(10000,15,3))
print(mul(10,20))