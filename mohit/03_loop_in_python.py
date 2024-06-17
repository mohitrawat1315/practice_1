#loops 
#repetition of same kind of work
#why you need & where it use..

#for loop
#while loop

#initalizing value
#loop condition
#updating value

# for loop|

my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)

name = ["m","0","h","i","t"]
for character in name :
    print(character)

# USING FOR LOOP with  USEING IF CONDITION

name = ["m","0","h","i","t"]
for character in name :
    print(character)
    if character in ["i"] :
        print("its special character")



#print "hello" five times
#ex

a = "hello"
print((a + " ")* 5)

#ex2 method 2

i = 1
while i <= 5 :
    print("hello",end= " " )
    i += 1 


count = 5 
while (count > 0) :
    print(count)
    count -= 1

#print all number form 1 to 40 using loop

i = 1 
while i <= 15 :
    print(i)
    i += 1
     




#range function (start, end ,jump)

# Here start is 0 and jump is 1

a = list(range(5))      #in range start is included end is excluded
print(a)


# by default jump here will be 1

b = list(range(1, 5))
print(b)


# start is included and end is excluded
c = list(range(1, 10, 2))
print(c)


# print 1 to 5  bye use loop condition 
# both for and while...


i = 1
while (i<=5):
    print(i)
    i += 1

for i in range(1,6):
    print(i)
    
    


for i in range(5):
    i += 1
    print(i)
   


# print even number in given range    

i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1 


number = [1,2,3,4,5,6,7,8,9,10]
for i in number :
    if i % 2 == 0:
        print(i)
    


# print even number in given range   


i = 0
while i <= 10:
    if i % 2 == 1:
        print(i)
    i += 1     


number = [1,2,3,4,5,6,7,8,9,10]
for i in number :
    if i % 2 == 1:
        print(i)
  


for i in range(1,11) :
    if i % 2 == 1:
        print(i,end=" ")
  
# multipilcation table


for i in range(1,11):
    i *= 5
    print(i)


for i in range(1,11):
    i /= 5
    print(i)

for i in range(1,11):
      i += 5
      print(i) 



'''also doing  with  input function
 Print Multiplication table '''

n = int(input("enter your number : "))
for i in range(1,11):
     print(i * n)

 
n = int(input("enter your number : "))
for i in range(1,11):
     print(i + n) 



for i in range(4):
    for i in range(8):
     print("#",end=" " )
    print( "\n")    

for j in range(5):
   for h in range(7):
      print("$",end=" ")
   print("\n")  


for i in range (1):
    for j in range(1):
        print("#",end=" ")
    print( )     
    for k in range(2):
        print("#",end=" ")   
    print( ) 
    for l in range(3):
        print("#",end=" ")
    print( )     
    for m in range(4):
        print("#",end=" ")   
    print( )          
