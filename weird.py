if __name__=='__main__':
   n=int(input().strip())
    if n>1 and n<=100:
        if n%2==1:
            print('weird')
        else:
            if n>=2 and n<=5:

                print('not weird')
            elif n>=6 and n<=20:
                print('weird')
            else:
                print('not weird')

