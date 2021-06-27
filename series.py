n=int(input('enter series range: '))
a=0
b=0
c=1
print(a,b,c,end=' ')
for i in range(3,n+1):
      d=a+b+c
      a=b
      b=c
      c=d
      print(d,end=' ')
