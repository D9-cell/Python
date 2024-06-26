age = int(input("Enter your age : "))

day = input("Which day of week is today : ")

price = 12 if(age >= 18) else 8
if(day.lower() == "wednesday"):
    price -= 2
print("Ticket Price for you is : $",price)
