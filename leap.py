#(c) Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not. (Hint Use the % (modulus) operator)

year=int(input("Enter the year : "))

if(year %4==0):
    if(year %100 ==0):
        if(year%400):
            print("leap year")
        else:
            print(" Not Leap Year")
    else:
        print("leap year")
else:
    print("not leap yaer ")