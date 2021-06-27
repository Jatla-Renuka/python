n=int(input())
rem=0
s=''
while True:
    rem=n%2
    print(rem)
    s+=str(rem)
    n=n//2
    if n<=1:
        print(1)
        s+=str(1)
        break

print('4th bit',s[3])    
