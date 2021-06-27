n=int(input('enter a number: '))
s=int(input('enter a start point: '))
e=int(input('enter end point: '))
if s<e:
    for i in range(s,e+1):
        print(n,'*',i,'=',n*1)
else:
    for i in range(s,e-1,-1):
      print(n,'*',i,'=',n*i)
