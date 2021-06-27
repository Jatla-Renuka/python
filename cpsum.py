def cpsum(t):
   s=0
        while t:
      rem=t%10
        t=t//10
        s+=cp(rem)
    return s
t=int(input())
print(cpsum(t))
