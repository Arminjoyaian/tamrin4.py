#number1 = int(input("Enter number1 :"))
#number2 = int(input("Enter number2 :"))
import math
print("1.- , 2.* , 3.+ , 4./ ")
print("log , sin , tan , cos ")
a = 0
op = int(input("Enter number?"))
if op ==1:
    num1=int(input("f num:"))
    num2=int(input("s num:"))
    print(num1 - num2)
elif op == 2:
    num1=int(input("f num:"))
    num2=int(input("s num:"))
    print(num1 + num2)
elif op == 3:
    num1=int(input("f num:"))
    num2=int(input("s num:"))
    print(num1 * num2)
elif op == 4:
    num1=int(input("f num:"))
    num2=int(input("s num:"))
    print(num1 / num2)
else:
    math.pow(TabError)    

mun1 = float(input("enter a mun:"))
if op == 5:
    a = math.log(mun1)
elif op == 6:
    a = math.sin(math.radians(mun1)) 
elif op == 7:
    a = math.cos(math.radians(mun1))       
elif op == 8:
    a = math.tan(math.radians(mun1))  
else:
    print("Again")        