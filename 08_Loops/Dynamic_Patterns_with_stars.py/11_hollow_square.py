rownum = int(input("Enter row number: "))

for i in range(rownum):
    for j in range(rownum):
        if ( j == rownum-1 or j == 0 or i == 0 or i == rownum-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()