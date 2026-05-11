n=int(input())
sum=0
dup=n
while n>0:
    r=n%10
    sum=sum+(r**3)
    n=n//10
    if sum==dup:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
    