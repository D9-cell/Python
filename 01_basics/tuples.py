tea_types = ("Black","Green","Oolong")
print(tea_types[0]) # Black
print(tea_types[-1]) #Oolong
print(tea_types[1:]) #('Green', 'Oolong')
#tea_types[0] = "Lemon" # --> this gives us error as tuples are immutable
# |--->TypeError: 'tuple' object does not support item assignment

more_tea = ("Herbal","Earl Grey")
all_tea = tea_types + more_tea
print(all_tea) # --> ('Black', 'Green', 'Oolong', 'Herbal', 'Earl Grey')

more_tea = ("Herbal","Earl Grey","Herbal")
print(more_tea.count("Herbal")) # --> 2
print(more_tea.count("herb")) # --> 0 (as herb is not present in more_tea)

(black,green,oolong) = tea_types # Here the number of items in both side must be same
print(black) # --> 'Black' 
print(green) # --> 'Green'
print(oolong)# --> 'Oolong' 

print(type(tea_types)) # --> <class 'tuple'>