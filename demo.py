# positive or negative
a=int(input("enter a number"))
if(a < 0):
     print( "is a negative")
elif (a == 0):
     print(" is zero")
else:
     print("is positive")
print()
# enven or odd
if(a %2 ==1):
     print(" is odd")
else:
     print("is even")
# age
age =int(input('enter you age :'))
if (age < 0):
     print('invalid')
elif(age >= 18):
     print('eligible for vote')
else:
     print('not eligible for vote')
#finding greater number  
a,b = map(int,input('enter two numbers').split())
print("is greater") if(a > b) else print("b is greater") 
# # marks
marks =int(input('enter marks'))
if(marks > 40):
     print('student is pass')
else:
     print('student is fail')
#  days
a=int(input('enter a number'))
if(a == 1):
     print("sunday")
elif(a == 2):
     print("monday")
elif(a == 3):
     print("tuesday")
elif (a == 4):
     print("wednesday")
elif(a == 5):
     print("thrusday")
elif(a==6):
     print("friday")
elif(a==7):
     print("saturday")
else:
    print("invalid")
#calculater 
optr =input("enter operation to perform")
inp1= float(input("enter  first number"))
inp2= float(input("enter second number"))
if (optr == 'add'):
     print(inp1 + inp2)
elif(optr == 'sub'):
     print(inp1 - inp2)
elif(optr == 'mul'):
     print(inp1 * inp2)
elif(optr == 'div'):
     print(inp1 / inp2)
else:
     print('invalid')