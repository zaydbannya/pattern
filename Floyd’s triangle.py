row=int(input("please enter the total number of rows"))
number=1
print("floyd's triangle")
for i in range(1,row+1):
    for j in range(1,i+1):
        print(number,end=' ')
        number=number+1
    print()