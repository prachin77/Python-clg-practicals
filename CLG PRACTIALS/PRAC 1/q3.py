from random import randint

randNum = randint(0,1000)
print(randNum)

ans = 0
s = randNum
while(s!=0):
    n = s%10
    ans=ans+n
    s=s//10

print("addition of individual digits : ",ans)