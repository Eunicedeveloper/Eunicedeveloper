#enable user to enter input
weight = input("enter weight in kgs")
height = input(" enter height in meters")


weight = float(weight)
height = float(height)

result = weight/(height * height)

print( " Your BMI is", result)

