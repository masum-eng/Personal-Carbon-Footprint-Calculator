from tips import show_tips

def calculate_and_show(calc):
    # Calculate each transport
    car_co2 = calc.car_km * calc.factors["car"]
    motorcycle_co2 = calc.motorcycle_km * calc.factors["motorcycle"]
    bus_co2 = calc.bus_km * calc.factors["bus"]
    train_co2 = calc.train_km * calc.factors["train"]

    transport_co2 = car_co2 + motorcycle_co2 + bus_co2 + train_co2

    electricity_co2 = calc.electricity * calc.factors["electricity"]
    food_co2 = (calc.meat_meals * calc.factors["meat"] +
                calc.veg_meals * calc.factors["vegetarian"] +
                calc.vegan_meals * calc.factors["vegan"])
    waste_co2 = calc.waste * calc.factors["waste"]

    total = transport_co2 + electricity_co2 + food_co2 + waste_co2

    # Eco Score
    if total <= 5:
        score = 95
        level = "Excellent"
    elif total <= 10:
        score = 80
        level = "Good"
    elif total <= 15:
        score = 65
        level = "Average"
    elif total <= 20:
        score = 50
        level = "Below Average"
    else:
        score = 30
        level = "Needs Improvement"

    # Show Result
    print("\n" + "="*55)
    print("           YOUR CARBON FOOTPRINT RESULT")
    print("="*55)
    print(f"Car            : {car_co2:6.2f} kg CO2")
    print(f"Motorcycle     : {motorcycle_co2:6.2f} kg CO2")
    print(f"Bus            : {bus_co2:6.2f} kg CO2")
    print(f"Train          : {train_co2:6.2f} kg CO2")
    print(f"Electricity    : {electricity_co2:6.2f} kg CO2")
    print(f"Food           : {food_co2:6.2f} kg CO2")
    print(f"Waste          : {waste_co2:6.2f} kg CO2")
    print("-"*55)
    print(f"TOTAL          : {total:6.2f} kg CO2  (today)")
    print("="*55)
    print(f"\nYour Eco Score : {score} / 100")
    print(f"Level          : {level}")
    print("="*55)

    # Automatic Tips
    show_tips(transport_co2, electricity_co2, food_co2, waste_co2)
    