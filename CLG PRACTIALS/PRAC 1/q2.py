import sys
from datetime import datetime as dt
# print(dt.now())
n=0
name=""
age=0
while(n!=4):
    print("1. ENTER DETAILS")
    print("2. SUBMIT")
    # print("3. SHOW DATE & TIME OF FORM SUBMISSION")
    print("4. EXIT")
    n = int(input("enter number = "))
    if(n==1):
        name = input("enter name : ")
        age = int(input("enter age : "))
    elif(n==2):
        print(f"{name} filled form successfully")
        cur_time = dt.now()
        print("form filling date = ",cur_time.strftime("%dth-%b-%Y"))
        print("form filling time = ",cur_time.strftime("%I"+":"+"%M"+":"+"%S"+" "+"%p"))
        print("FORM SUBMITTED")
    elif(n==4):
        sys.exit()
    else:
        print("wrong number is entered")
