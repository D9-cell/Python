order_size = "Medium"
extra_shot = True

coffee = ""
if(extra_shot):
    coffee = order_size + " Coffeee with an extra shot"
else:
    coffee = order_size + " Coffee"
    
print("Your  ",coffee)