choice = input("What input you want ?")
if choice == "kmh":
    print("What is the distance in Km ?")
    km = input()
    print(f"You said {km} km")
    miles = float(km) * 0.621371
    miles = round(miles,2)
    print(f"{km} kilometers are equivalent a {miles} miles.")
elif choice == "mph":
    print("What is the distance in Miles ?")
    miles = input()
    print(f"You said {miles} miles")
    km = float(miles) * 1.61
    mkm = round(km,2)
    print(f"{miles} miles are equivalent a {km} kilometers.")
else:
    print("This is not a valid choice, valid choices are kmh or mph")
opinion = input("Are you happy from the result ?")
if opinion == "yes":
    print("Valeu")
