n=int(input("Enter: "))
if n==0:
    print("False")
while n>0:
    if n==1:
        print("True")
    if n%2!=0:
        break
    n=n//2
print("False")