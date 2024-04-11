def bubbleSort(l,n):
    for i in range(n):
        for j in range(i+1,n):
            if(l[j]< l[i]):
                tmp = l[j]
                l[j] = l[i]
                l[i] = tmp

    for i in l:
        print(i," ")

def insertionSort(l, n):
    for i in range(1, n):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            tmp = l[j]
            l[j] = l[j - 1]
            l[j - 1] = tmp
            j = j - 1

    for i in l:
        print(i, " ")


n = int(input("enter list length = "))
l = []
for i in range(n):
    ele = int(input("enter number = "))
    l.append(ele)

print("1. BUBBLE SORT")
print("2. INSERTION SORT")
choice = int(input("enter choice = "))
if(choice == 1):
    bubbleSort(l,n)
elif(choice == 2):
    insertionSort(l,n)
else:
    print("wrong choice")