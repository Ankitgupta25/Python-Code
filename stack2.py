l=[]
while True:
    c = int(input('''
1 push Element
2 pop Element
3 peek Element
4 Display Element
5 Exit
'''))
if c==1:
    l.append()
    print(l)
elif c==2:
  if  len(l)==0:
    print("Empty stack")
  else:
      l.pop[-1]
elif c==3:
    if len(l)==0:
     print("Empty stack")
    else:
     print(l[-1])
elif c==4:
    print("Display Element", l)
elif c==5:
  exit[0]
else:
    print("invalid operation")
    