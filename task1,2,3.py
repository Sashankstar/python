num1=3333
num2=5454
# print(num1)
#print(num2)
num2=630384
#print(num2)
#print(num2)
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1&num2)
# print(num1**num2)....It is not applying
print(num1//num2)

#Datatype
print(type(num1))
print(type(num2))


#Strings
name1= 'nikhil'
print(name1)
name2="sashank"
print(name2)

#length
print(len(name1))
print(len(name2))

#String Indexing
print(name1[5])
print(name2[2])

#Negative Indexing
print(name1[-2])
print(name2[-4])

#slicing (or) Substring
print(name1[2:10])
print(name1[5:8])

#Negative Slicing
print(name1[-12:-2])
print(name2[-8:-1])

#Datatypes
#1.Numeric data types
#2.Sequence Data types

#Numeric Data types
#1.Int data type
#2.Float data type
#3.Complex number data type
#4.Boolean data type

#Int Data type
a=21345
b=45637
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(type(a))
print(type(b))

#float Data type
r=5.11
m=5.5
print(r+m)
print(r-m)
print(r*m)
print(r/m)
print(r//m)
print(r**m)

#Float class
print(type(r))
print(type(m))

#complex number data type
t=8
n=5j
print(t+n)
print(t-n)
print(t*n)
print(t/n)
# print(t//n) unsupported operand
print(t**n)


#Complex class
print(type[t])
print(type(n))

#Boolean data type
#True condition
surya=2420
arun=2420
print(surya==arun)

#False condition
surya=2420
arun=2423
print(surya==arun)

#Boolean class
print(type(surya==arun))

#Boolean length
# print(len(vamshi==raghu))....objects of boolean has no length

#Sequence Data types
#1.string data type
str1= 'Ten thousand coders'
str2= 'python classes'
print(str1)
print(str2)

#String lenght
print(len(str1))
print(len(str2))

#String append
str1 +="kphb"
print(str1)

#string class
print(type(str1))

#List data types
list1=[1,2,3,name1,[True,2025],2+5j,[False,2024],3020]  
print(list1)

#length
print(len(list1))

#list type
print(type(list1))

#List indexing
print(list1[6])

#Slicing
print(list1[2:8])
print(list1[-5:-1])

#List Append
list1.append(89)
print(list1)
print(len(list1))

#Tuple Data type
tup=(2,5,8,str,5678,__name__,[2,5j,-55],[-7,name1,2.5],25,3.9,7j)
print(tup)
print(type(tup))

#tuple append 
tup +=(2+3j,)
print(tup)

#length tuple
print(len(tup))

#Slicing
print(tup[2:10])
print(tup[-12:-4])