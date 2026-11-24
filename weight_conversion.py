print("***Weight Convertor***")
print("Enter the conversion: ")
print("""    1. kilogram(kg) to gram(g)
    2. gram(g) to (kg)
    3. kilogram(kg) to pounds(lbs)
    4. pounds(lbs) to kilogram(kg)
    5. gram(g) to milligram(mg)
    6. milligram(mg) to gram(g)
    7. exit""")
convert = int(input("Enter the conversion(1 to 7): "))

if(convert == 1):
    kg = float(input("Enter the kg: "))
    g = kg * 1000
    print(f"Gram for {kg} kg = {g}g")
elif(convert == 2):
    g = int(input("Enter the g: "))
    kg = g // 1000
    print(f"Kilogram for {g} g = {kg} kg")
elif(convert == 3):
    kg = float(input("Enter the kg: "))
    lbs = kg // 0.45
    print(f"lbs for {kg} kg = {lbs}lbs")
elif(convert == 4):
    lbs = float(input("Enter the lbs: "))
    kg = lbs * 0.45
    print(f"kg for {lbs} lbs = {kg} kg")
elif(convert == 5):
    g = float(input("Enter the g: "))
    mg = g *1000
    print(f"MilliGram for {g}g = {mg}mg")
elif(convert == 6):
    mg = float(input("Enter the mg: "))
    g = mg // 1000
    print(f"Gram for {mg} mg = {g} g")
elif(convert == 7):
    print("exiting...")
else:
    print("invalid input")