#want to show something as output : use print function
#() bracket we call parentheses
print("hello world")
print("world") 

"""  variable are place holder for storing data
variable name cannot start with number (0-4)
variable are case sensitive(age,Age and AGE all are different variable)
variable name start with a letter or the underscore char. (a-z,A-Z,_(underscore))
x(variable name)=12(value to be assigned)  """

a = 4
print(a)

#variable name can only contain alph numeric characters and underscore (a-z,A-Z,_(underscore))
mohit_12 = 5 
print(mohit_12)

#3a=56  
#variable name cannot start with number (0-4)

#inbuilt keywords cannot use as variable
help("keywords")
#for=89
#break=70

#for comments we use hash(#)

#data type in python
#Intergers (-9,0,9)
#Float     (-9.4,8.8) decimal use 
#Booleans  (True,False)
#String    (any thing which is inside coths )
#None

#IF YOU WANT TO KNOW WHAT DATA TYPE IS THIS 
#WE USE TYPE  FUNCTION

#Intergers 
a = 42
print(type(a))
print(a)

#Float  
b = 2.3
print(type(b))
print(b)

#Booleans
c = True
print(type(c))
print(c)

#String 
d = "hello 3 @"
print(type(d))
print(d)

#None
g = None
print(g)
print(type(g))

""" print function we can use multiple vaules under print function 
just by seprating using the a coma """

print("rahul", "mohit", 52, 47, 4.5 ,"mohit_12")

#python operator
#operator(+,-,*,/,//,**) these are operator 
#operands(x,y)
#combine then its call an expression
#operator + operands = expression


#Arithmetic Operators

e = 5
f = 9
#Addition
print(e+f)

#Subtraction
print(e-f)

#Division  division operator always give float values
print(e/f)

#modulus (%) it will give remainder
print(e%f)

#multiplication
print(e*f)

#floor division (//) the result is floored to the nearest smaller integer means on left side of number line 
print(e//f)

#to the power(**)   5*5*5*5*5**5*5*5 (9times)
print(e**f)

#string concatenation
first = "mohit"
last = "rawat"
print(first +  last)
print(first * 3)

#COMPARISON OPERATORS are use where we compare two  value the answer is alway the booleans value

#==(True if equal )
#!=(Trueif not equal)
#<(less then) & >(greater  then)
#<=(less then or equal to) & >=(greater then or equal to)

a=8
b=6
print(a == b)

print(7 == 7)

print(a != b)

print(a > b)

print(a < b)

print(a >= b)

print(a <= b)


#ASSIGNMENT OPERATORS
# =
# -=
# +=
# /=
# *=

a = 8

#a = a + 3 is same as a+=3  same with other assignment operators
a += 4
print(a)

a-=14
print(a)

a /= 6
print(a)

a *= 8
print(a)


#LOGICAL OPERATORS
#Its is part of electroni and communication part of eggenerring

#and
#or
#not

#these gate work on booleans value...

"""True and True
True and False
False and False
False and True """

3 > 4

4 > 3

3 > 4 and 4 > 3

4 > 3 and 3 > 2

# just like or operators  work on two values 

#or

"""True or True  #Ture   3 > 2 or 4 > 3
True or False    #True   3 > 2 or 2 > 3
False or True    #True   2 > 3 or 3 > 2
False or False   #False  2 > 3 or 2 > 3  """

#not 
# just like or operators  work on two values

#not False
not 2 > 3

#not True
not 3 > 2



