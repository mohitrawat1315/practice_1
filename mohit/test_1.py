# a = list(range(5))
# print(a)


for i in range(1,11):
    i *= 5
    print(i)


for i in range(1,11):
    i /= 5
    print(i)

for i in range(1,11):
      i += 5
      print(i) 

# also doing  with  input function
# Print Multiplication table
n = int(input("enter your number : "))
for i in range(1,11):
     print(i * n)