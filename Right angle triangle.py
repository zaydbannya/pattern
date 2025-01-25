print("half pyramid of stars(*):")
n=int(input("enter the number of row:"))
for i in range(n):
    for j in range(i+1):
       print("*",end="")
    print()