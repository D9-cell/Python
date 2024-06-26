chai_types = {
    "Masala":"spicy",
    "Ginger":"zesty",
    "Green":"Mild"
}
print(chai_types["Masala"]) # --> spicy
print(chai_types.get("Masala")) # --> spicy

chai_types["Green"] = "Fresh"
print(chai_types.get("Green")) # --> "Fresh

for chai in chai_types:
    print(chai) # --> Masala Ginger Green (Prints the keys)
    
#in python every key,value pair is known as "Item"
for chai in chai_types:
    print(chai,chai_types.get(chai)) # --> Masala spicy Ginger zesty Green Fresh (Prints in key value pair)
    
for chai,chais in chai_types.items():
    print(chai,chais)# --> Masala spicy Ginger zesty Green Fresh (Prints in key value pair)

chai_types["earl Grey"] = "Citrus" # --> we can add item by this process
print(chai_types)

valueOfitem = chai_types.pop("Ginger") #--> In Dictionary we have to pass the key which we want to delete and this will return the value of the key
print(valueOfitem) # --> zesty which is value of "Ginger"

item = chai_types.popitem() # --> popitem method will delete which is inserted last at the dictionary
print(item) # --> " ('earl Grey', 'Citrus') " retrun in this format

del chai_types["Green"] # --> "del" will delete from memory references 

print(chai_types)

## In dictionary  we can have dictionaries in dictionary
tea_shop = {
    "chai" : { "Masala":"Spicy" , "Ginger":"zesty" },
    "Tea" : { "Green":"Mild" , "black":"strong" }
}

print(tea_shop.get("chai"))# --> {'Masala': 'Spicy', 'Ginger': 'zesty'}
print(tea_shop["chai"]) # same output as the above

print(tea_shop.get("chai").get("Ginger")) # --> zesty
print(tea_shop["chai"]["Ginger"]) # same output as above


squared_num = {x:x**2 for x in range(6)}
print(squared_num) # --> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

squared_num.clear() # --> this will deleted all the items in the squared_num

keys = ["Masala","Ginger","Lemon"]
default_values = "delicious"

new_dict = dict.fromkeys(keys,default_values)
print(new_dict) # --> {'Masala': 'delicious', 'Ginger': 'delicious', 'Lemon': 'delicious'}

#Below we have discussed a default nature of python
new_dict = dict.fromkeys(keys,keys)
print(new_dict) # --> {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}







