l=[]
while True:
    c=int(input('''
    1 push Element
    2 pop  Element
    3 Front Element
    4 Last Element
    5 Display Queue
    6 Exit
    '''))
    if c==1:
        n=input("Enter the value:-")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("empty queue")
        else:
            l.pop(0)
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty queue")
        else:
            print(l[0])
    elif c==4:
        if len(l)==0:
            print("empty queue")
        else:
            print(l[-1])
    elif c==5:
        print(l)
    elif c==6:
        break;
    else:
        print("invalid operation")



