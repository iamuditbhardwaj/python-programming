rownum = int(input("Enter number of rows: "))

for i in range(rownum):
    for j in range(rownum - i):
        print("*",end=" ")
    print()