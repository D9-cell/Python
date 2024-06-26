tea_varities = ["Black","Green","Oolong","white"]
#print(tea_varities)
tea_varities[1:2] = "Lemon"
#print(tea_varities) # --> ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'white']

tea_varities = ["Black","Green","Oolong","white"]
tea_varities[1:2] = ["Lemon"]
print(tea_varities) # --> ['Black', 'Lemon', 'Oolong', 'white']

tea_varities[1:3] = ["Green","Lemon"]
print(tea_varities) # --> ['Black', 'Green', 'Lemon', 'white']

tea_varities[1:3] = ["Green"]
print(tea_varities) # --> ['Black', 'Green', 'white']

tea_varities[1:1] = ["Lemon","Adrak"]
print(tea_varities) #--> ['Black', 'Lemon', 'Adrak', 'Green', 'white']

tea_varities[1:3] = [] #Insert nothing operation that actually means deletion
print(tea_varities) # --> ['Black', 'Green', 'white']


for tea in tea_varities:
    print(tea)

for tea in tea_varities:
    print(tea,end="-")
    
if "Oolong" in tea_varities:
    print("Yes I have Oolong tea")
else:
    print("No i dont have it.")
    
tea_varities.append("Oolong") #--> append at the last position of the list
print(tea_varities)

var = tea_varities.pop()  #delete the last value stored at the list
print(var) #--> Oolong
print(tea_varities) # --> ['Black', 'Green', 'white']

val = tea_varities.remove("Green") # --> this return nothing
print(val) # as remove returns nothing so val=None

print(tea_varities) # --> ['Black', 'white']
tea_varities.insert(1,"Oolong")
print(tea_varities) # --> ['Black', 'Oolong', 'white']

tea_varities_copy = tea_varities.copy() # now both are pointing to different memory reference in memory

squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_number = [x**3 for x in range(10)]
print(cube_number)
