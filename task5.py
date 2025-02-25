# to print the number is prime or not
num=int(input("Enter the number"))
flag=True 
for i in range(2,num):
    if num%2==0:
        print(num,"is not a prime num")
        flag=False
        break

if flag:
    print(num,"is a prime num") 
         
        
#  to print 3 and 5 multiples
for i in range(1,100):
    if i%5==0:
        print(i)
    elif i%3==0:
        print(i)
    
# to print Fibonacci numbers
fibo=int(input("Enter the number"))
a,b=0,1
for i in range(fibo):
    print(a,end=' ')
    a,b=b,a+b