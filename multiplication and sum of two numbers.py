# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

a=int(input("enter first number; "))
b=int(input("enter sec number; "))
d=a*b
e=a+b
if (d<=1000):
  print(d)
elif (e>1000):
  print(e)
