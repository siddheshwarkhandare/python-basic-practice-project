#n=int(input("enter your no!"))
n=5
for i in range(n-1):
    p=1
    for j in range(i,n):
        print("*", end="")
        p+=1
    print()
for i in range(n):
    k=1
    for j in range(i+1):
        print("*", end="")
        k+=1
    print()