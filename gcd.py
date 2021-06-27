num1=24
num2=12
while True:
    if(num1>=num2):
        num1=num1-num2
    else:
        num1,num2=num2,num1
    if num1==0:
        break
   print(num2)
