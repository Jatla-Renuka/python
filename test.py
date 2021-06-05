a=float(input('enter 1 st side:'))
b=float(input('enter 2 nd side:'))
c=float(input('enter 3 rd side:'))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of triangle is %0.2f'%area)
