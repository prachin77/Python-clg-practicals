from random import randint

def q1():
    # Get user input for the amount
    amount = float(input("Enter an amount in decimal , for example 11.56: "))

    # Calculate the total cents
    total_cents = int(amount * 100)

    # Calculate the number of dollars
    dollars = total_cents // 100
    remaining_cents = total_cents % 100

    # Calculate the number of quarters
    quarters = remaining_cents // 25
    remaining_cents %= 25

    # Calculate the number of dimes
    dimes = remaining_cents // 10
    remaining_cents %= 10

    # Calculate the number of nickels
    nickels = remaining_cents // 5
    remaining_cents %= 5

    # The remaining cents are the number of pennies
    pennies = remaining_cents

    # Output the result
    print(f"Your amount {amount:.2f} consists of")
    print(f"{dollars} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{nickels} nickels")
    print(f"{pennies} pennies")


def q2():
    print("Q2")
    # q2
    randNum = str(randint(10,99))
    print(randNum)
    n = input("enter number (RANGE 10 - 99) : ")
    # toString = str(randNum)
    c = 0
    # print(type(toString)," ",type(n))
    if n == randNum:
        print("you won $10,000")
        # 56 | 65
    elif ((randNum[0] == n[0] or randNum[0] == n[1]) and (randNum[1] == n[0] or randNum[1] == n[1])):
        print("you won $5,000")
    elif ((randNum[0] == n[0] or randNum[0] == n[1]) or (randNum[1] == n[0] or randNum[1] == n[1])):
        print("you won $2,000")
    else:
        print("wrong number")


def q3():
    print("Q3")
    randNum = randint(0,100)
    # r-45 | n-63
    # r-45 | n-25
    # print(randNum)
    n = int(input("enter number : "))
    tmp = 0
    tmp1 = 0
    if n == randNum:
        print("yes the number is ",n)
    else:
        while n!=randNum:
            n = int(input("enter number : "))
            if n == randNum:
                print("there you go 👌 the number is ",n)
                break
            if n < randNum:
                tmp = randNum - n
                if tmp >= 20:
                    print("you guess is too low make it closer")
                elif tmp >= 10 and tmp <= 20:
                    print("you guess is quite low make it closer")
                elif tmp <= 10:
                    print("you're close to you target")
            if n > randNum:
                tmp1 = n - randNum
                if tmp1 >= 20:
                    print("you guess is too high make it closer")
                elif tmp1 >= 10 and tmp1 <= 20:
                    print("you guess is quite high make it closer")
                elif tmp1 <= 10:
                    print("you're very close to you target")

def main():
    print("1. Q1")
    print("2. Q2")
    print("3. Q3")
    n = int(input("enter number : "))
    if n == 1:
        q1()
    elif n == 2:
        q2()
    elif n == 3:
        q3()
    else:
        print("wrong number")
main()