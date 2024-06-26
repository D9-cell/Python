score = 99

if(score > 100):
    print("Value is not accepted.")
    exit()
grade = "F"
if (score >= 90):
    grade = "A"
elif(score >= 80):
    grade = "B"
elif(score >= 70):
    grade = "C"
elif(score >= 60):
    grade = "D"
else:
    grade = "F"
    
print("Your Grade is : ",grade)
