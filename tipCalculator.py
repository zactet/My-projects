print("Welcome to the tip calculator.")
total = float(input("What was the bill total?: $"))
people = int(input("How many people to split the bill?: "))
tip = int(input("What percentage would you like to tip?(e.g. 10,12,15): "))
tip_converted = tip / 100 +1
pay = (total / people) * tip_converted
print(f"Each person should pay ${pay:.2f}.")