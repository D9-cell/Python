while(True):
    number = int(input("Enter Number between 1 and 10 : "))
    if(1 <= number <= 10):
        print("Thanks.")
        break
    else:
        print("invalid Input,Try Again.")