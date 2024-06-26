weather = "Sunny"

activity = ""

if(weather.lower() == "sunny"):
    activity = "Go for a walk"
elif(weather.lower() == "rainy"):
    activity ="Read a book"
elif(weather.lower() == "snowy"):
    activity = "Build a Snowman"
    
print(activity)