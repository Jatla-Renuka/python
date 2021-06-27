n=int(input('enter nummber: '))
rev=0
temp=n
while n!=0:
 r=n%10
 rev=rev*10+r
 n=n//10
 if temp==rev:
     print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")
