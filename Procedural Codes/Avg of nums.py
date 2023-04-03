n=int(input("how many numbers: "))
sum=0
for i in range(0,n):
  num=float(input("enter numbers: "))
  sum+=num
avg=sum/n
print(avg)
