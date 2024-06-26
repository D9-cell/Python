n = int(input("Enter the value of N : "))

sum = 0
for i in range(1,n+1):
    if(i%2 == 0):
       sum += i
       
print("Sum of All even numbers in Range is ",sum) 