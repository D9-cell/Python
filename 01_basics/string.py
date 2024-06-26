chai = "Masala chai"
first_char = chai[0]
print(first_char)
slice_chai = chai[0:6]
print(slice_chai)
num_list = "0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[0:7:3])

print(chai.lower())
print(chai.upper())

chai = "   Masala Chai   "
print(chai.strip())
chai = "Lemon Chai"
print(chai.replace("Lemon","Ginger"))
chai = "Lemon, Ginger, Masala, Mint"
print(chai) #Lemon, Ginger, Masala, Mint    
print(chai.split(", ")) # --> ['Lemon', 'Ginger', 'Masala', 'Mint']

chai = "Masala Chai"
print(chai.find("Chai"))
print(chai.find("chai")) #--> if it doesn't find then return -1

chai = "Masala Chai Chai Chai"

print(chai.count("Chai"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai" # {} --> this is placeholder in html
print(order.format(quantity,chai_type))

chai_variety = ["Masala","Ginger","lemon"]
print(" ".join(chai_variety)) # --> Masala Ginger lemon
print(", ".join(chai_variety)) # -->Masala, Ginger, lemon
chai = "Masala Chai"
print(len(chai))

for letter in chai:
    print(letter)
    
chai = "he said, \" Msasala Chai is awesome\""
print(chai)
chai = "Masala\nChai"
print(chai) # print Masala and chai in two lines and dont treat chai as a raw string

chai = r"Masala\nChai" # Now 'r' putting before a string means treat this string as a raw string and \n treat as a string not a as new line
print(chai)
#chai = "masala chai"
#print("masala" in chai) # --> True
#print("maasala" in chai) # --> False
