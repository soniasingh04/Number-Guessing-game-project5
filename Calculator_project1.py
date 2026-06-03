#python program to create a simple calculator
#1.functions for operations
#2.user input
#3.print result

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

def avg(num1,num2):
    return (num1+num2)/2
print("please select a operation :\n"\
        "1.Addition\n"\
        "2.Subtarction\n"\
         "3.Multiplication\n"\
         "4.Division\n"\
         "5.Average\n")


select =int(input("select a operation from 1,2,3,4,5:"))
num1=int(input("enter the number1 :"))
num2=int(input("enter the number2 :"))


if select==1:
    print(num1 ,"+", num2 ,"=", \
          add(num1,num2))
elif select==2:
    print(num1 ,"-", num2 ,"=", \
          subtract(num1,num2))
elif select==3:
    print(num1 ,"*", num2 ,"=", \
          multiply(num1,num2))
elif select==4:
    print(num1 ,"/", num2 ,"=", \
          divide(num1,num2))
elif select==5:
    print("(",num1 ,"+", num2,")","/","2" ,"=", \
          avg(num1,num2))     
else:
    print("invalid operation!please select again")               



