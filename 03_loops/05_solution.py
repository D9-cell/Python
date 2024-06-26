input_string = input("Write Your String : ")

for ch in input_string:
    print(ch)
    if(input_string.count(ch) == 1):
        print("Char is : ",ch)
        break