n=int(input())
n=bin(n)
n=n[2:]
n=n[::-1]
if len(n)<4:
    print(0)
else:
    print(n[3])
