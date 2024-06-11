#loops 
#repetition of same kind of work
#why you need & where it use..

#for loop
#while loop

#initalizing value
#loop condition
#updating value

#print "hello" five times
#ex

a = "hello"
print((a + " ")* 5)

#ex2 method 2

i = 0
while i <= 6 :
    print("hello",end= " " )
    i += 1 


count = 5 
while (count > 0) :
    print(count)
    count -= 1

#print all number form 1 to 40 using loop

i = 1 
while i <= 40 :
    print(i)
    i += 1
     




#range function (start, end ,jump)

# Here start is 0 and jump is 1

a = list(range(5))
print(a)


# by default jump here will be 1

b = list(range(1, 5))
print(b)


# start is included and end is excluded
c = list(range(1, 10, 2))
print(c)


for i in range(5):
    i += 1
    print(i)
   