for i in range(1,101):
    print(i)
# 2
a=int(input("enter a number"))
print((a*(a+1))/ 2)
# 3
even=[]
odd=[]
i=0
while i<= 50:
    if( i %2 ==0):
        even.append(i)
        i=i+1
    else:
        odd.append(i)
        i=i+1
print('even numbers: ',even)
print('odd numbers:',odd)
# 5
num=123345
rev_num=0
while num>0:
    rem = num % 10
    rev_num = rev_num *10 +rem
    num=num//10
print(rev_num)