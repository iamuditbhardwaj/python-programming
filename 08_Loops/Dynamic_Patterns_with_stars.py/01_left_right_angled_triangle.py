rownum = int(input("Enter number of rows: "))

for i in range(rownum):
    for j in range(i+1):
        print("*",end=" ")
    print()