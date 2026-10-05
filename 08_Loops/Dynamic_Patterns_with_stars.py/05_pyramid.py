rownum = int(input("Enter number of rows: "))

for i in range(rownum):
    for j in range(rownum-i-1):
        print(" ",end=" ")
    for k in range((2*i)+1):
        print("*",end=" ")
    print()