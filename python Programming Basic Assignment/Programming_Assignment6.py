'''Write a Python Program to Display Fibonacci Sequence Using Recursion?'''
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

num=int(input("Enter the Number"))
if num<=0:
    print("Fibonacci series can only be generated for positive number")
else:
    print("Fibonacci Series:")
    for i in range(num):
        print(recur_fibo(i))

'''Write a Python Program to Find Factorial of Number Using Recursion?'''
def recur(n):
    if (n==1):
        return n
    else:
        return n*recur(n-1)

num=int(input("Enter a number for Factorial: "))
if(num<0):
    print("Factorial of Negative Number do not exist")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    j=recur(num)
    print("Factorial of Number:",num,"is: ",j)

'''Program to Calculate BMI'''
def bmi(wt,ht):
    bmindex=bmi=wt/ht**2
    return bmindex
wt=float(input("Enter the weight in Kgs. : "))
if(wt>200):
    print("Enter Weight Below 200 Kgs")
else:
    ht=float(input("Enter the height of Mtrs. : "))
    if(ht>2):
        print("Enter Height Less than 2 Mtrs")
    else:
        bmivalue=bmi(wt,ht)
        print("BMI Index is : ",bmivalue)
        if(bmivalue<18.5):
            print("You are underweight")
        elif(bmivalue>=18.5 and bmivalue<=24.9):
            print("You are Normal Weight")
        elif(bmivalue>=25 and bmivalue<=29.9):
            print("You are Over Weight")
        elif(bmivalue>=30 and bmivalue<=35):
            print("You are Obese")
        else:
            print("SEVERE OBESITY")


'''Write a Python Program for cube sum of first n natural numbers?'''

num=int(input("Enter the Natural Number: "))
if (num<0):
    print("Enter a positive Number only")
else:
    sum=0
    for i in range(num+1):
        sum=sum+pow(i,3)

    print("Sum of Cube of a Natural Number: ",num,"is: ",sum)