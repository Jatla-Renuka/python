num=int(input())
res=0
while True:
    r=num%10
    res=res*10+r
    num=num//10
    if num==0:
        break
print(res)
