n,m = map(int,input("enter 2 numbers = ").split())
print(n," ",m)

def binaryMatrix(arr):
    isBinary = True
    for row in arr:
        for column in row:
            if column not in [0,1]:
                print("NOT BINARY MATRIX ")
                break
            print(column,end=" ")
        print("\n")
    print("YES BINARY MATRIX")

def identityMatrix(arr,n,m):
    isIdentity = False
    if n%2==0 and m%2==0 and n==m: 
        for i in range(n):
            for j in range(m):
                if j in [0,1]:
                    if i == j and arr[i][j] == 1:
                        isIdentity = True
                else:
                    print("contains no except 1 & 0")
                    break
        return isIdentity
    else:
        s = "can't check for identity matrix"
        return s

    
arr = []
for i in range(n):
    row = []
    print("ROW ",i+1)
    for j in range(m):
        print("COLUMN ",j+1,end=" ")
        num = int(input("enter num = "))
        row.append(num)
    arr.append(row)

print("1. BINARY MATRIX CHECK")
print("2. IDENTITY MATRIX CHECK")
n = int(input("enter number = "))
if n==1:
    binaryMatrix(arr)
elif n==2:
    print(identityMatrix(arr,n,m))
else:
    print("wrong number")
