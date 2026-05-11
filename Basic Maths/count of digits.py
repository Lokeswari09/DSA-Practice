n=int(input())
c=0
if n==0:
    count=1
else:
    while n>0:
        c=c+1
        n=n//10
    print(c)