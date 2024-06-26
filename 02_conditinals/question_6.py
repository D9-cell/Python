distance = 5

transport = ""
if(distance < 5):
    transport = "Walk"
elif (distance <= 15):
    transport = "Bike"
else:
    transport = "Car"
    
print("AI recomend : ",transport)
