#control flow 


a=int(input("enter your  age : "))
print("your age is a",a)
if(a>18):
    print("you can drive")
else:
    print("you cannot drive") 



x= int(input("enter the temperature : "))
if (x>40):
     print("it's a hot day")
elif(x<10):
     print("it's a cold day")
else :
     print("it's normal day")  
     

x = int(float(input("enter your number : ")))
if x > 0 :
    print("It's positive number")
elif x == 0 :
    print("It's zero") 
else :
    print("It's negitive numer")     


#range  function

for k in range (1,5) :
    print(k)


#reversed function
places = ["delhi", "uttarkhand", "mumbai","uttar pardesh"]
#for i in places :
 #   print(i)
for items in reversed(places):
    print(items)


colors = ["Red", "Green", "Blue"]
for color in reversed(colors):
    print(color)


#find max in a list
#find highest marks 
marks = [10, 50, 48, 100]   #list  element
highest = marks[0]
for i in marks: 
    if i > highest:
        highest = i
print(highest)

lowest = marks[0]
for g in marks:
    if g < lowest :
        lowest = g
print(lowest)        


