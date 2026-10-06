rownum = int(input("Enter number of rows: "))

if rownum%2 == 0:
    print("Please enter an odd number !!!!")
else:
    rownum = (rownum+1)//2

    for i in range(rownum):
        for j in range(i+1):
            print("*",end=" ")
        print()

    rownum = rownum - 1

    for i in range(rownum):
        for j in range(rownum-i):
            print("*",end=" ")
        print()       