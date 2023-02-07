n=int(input("enter num:\n"))
s=0
o=len(str(n))
n5=n
while(n>0):
  d=n%10
  s+=d**o
  n=n//10
if(s==n5):
    print(f"{n5} is armstrong")
else:
  print('smd bish')
