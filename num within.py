n=int(input())
def diff(n):

    if n<=100:
       return (f"{n} is within 100")
    elif n<=1000:
       return (f"{n} is within 1000")
    elif n<=2000:
       return (f"{n} is within 2000")
print(diff(n))
