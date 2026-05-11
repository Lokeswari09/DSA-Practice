n=int(input())
dup=0
rev=0
while n>0:
    r=n%10
    rev=(rev*10)
    n=n//10
    if dup==rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")