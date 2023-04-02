import random
comp=random.randint(0,2)
user=int(input("Enter 0 for snake, 1 for water, 2 for gun:\n"))
def check(comp,user):
  if comp==user:
    return 0
  if (comp==0 and user==1):
    return -1
  if comp==1 and user==2:
    return -1
  return 1
score=check(comp,user)
if score==0:
    print("draw")
elif score==1:
    print("u won")
elif score==-1:
    print("lost")
print("comp choose", comp)
print("user choose", user)
