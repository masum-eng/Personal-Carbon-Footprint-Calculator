# ============================================================
# Personal Carbon Footprint Calculator
# SDG 13: Climate Action
# BIT2083 - Fundamental of Computational Thinking: Python
# ============================================================

def display_menu():
    """Display the main menu of the application"""
    print("\n" + "="*55)
    print("       PERSONAL CARBON FOOTPRINT CALCULATOR")
    print("              (SDG 13 - Climate Action)")
    print("="*55)
    print("1. Calculate Electricity Emission")
    print("2. Calculate Transport Emission")
    print("3. Calculate Food Emission")
    print("4. Calculate Waste Emission")
    print("5. View Total Carbon Footprint & Tips")
    print("6. Reset All Data")
    print("7. Exit")
    print("="*55)

def get_positive_float(prompt):
    """Get a positive number from user with validation"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  Error: Value cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("  Error: Please enter a valid number.")

def calculate_electricity():
    """Calculate CO2 emission from electricity usage (kg CO2)"""
    print("\n--- Electricity Emission ---")
    kwh = get_positive_float("Enter monthly electricity usage (kWh): ")
    # Average emission factor: 0.5 kg CO2 per kWh (approximate)
    emission = kwh * 0.5
    print(f"Electricity Emission: {emission:.2f} kg CO2")
    return emission

def calculate_transport():
    """Calculate CO2 emission from transportation"""
    print("\n--- Transport Emission ---")
    print("1. Car / Motorcycle")
    print("2. Public Transport (Bus/Train)")
    print("3. Walking / Bicycle (0 emission)")
    
    while True:
        choice = input("Select transport type (1-3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("  Invalid choice. Please enter 1, 2 or 3.")

    if choice == '3':
        print("Transport Emission: 0.00 kg CO2 (Great choice!)")
        return 0.0

    km = get_positive_float("Enter total distance travelled this month (km): ")

    if choice == '1':
        # Average car: 0.21 kg CO2 per km
        emission = km * 0.21
    else:
        # Public transport average: 0.05 kg CO2 per km
        emission = km * 0.05

    print(f"Transport Emission: {emission:.2f} kg CO2")
    return emission

def calculate_food():
    """Calculate approximate CO2 from food consumption"""
    print("\n--- Food Emission ---")
    print("How many days per week do you eat meat/dairy heavily?")
    days = get_positive_float("Enter days (0-7): ")
    
    if days > 7:
        days = 7

    # Rough estimate: high meat diet ~ 7 kg CO2/day, low ~ 2 kg
    daily_emission = 2 + (days / 7) * 5
    monthly_emission = daily_emission * 30
    print(f"Food Emission (approx): {monthly_emission:.2f} kg CO2")
    return monthly_emission

def calculate_waste():
    """Calculate emission from household waste"""
    print("\n--- Waste Emission ---")
    kg_waste = get_positive_float("Enter approximate monthly waste (kg): ")
    # Average landfill emission ~ 0.5 kg CO2 per kg waste
    emission = kg_waste * 0.5
    print(f"Waste Emission: {emission:.2f} kg CO2")
    return emission

def show_results(electricity, transport, food, waste):
    """Display total carbon footprint and eco tips"""
    total = electricity + transport + food + waste
    print("\n" + "="*55)
    print("           YOUR MONTHLY CARBON FOOTPRINT")
    print("="*55)
    print(f"Electricity : {electricity:8.2f} kg CO2")
    print(f"Transport   : {transport:8.2f} kg CO2")
    print(f"Food        : {food:8.2f} kg CO2")
    print(f"Waste       : {waste:8.2f} kg CO2")
    print("-"*55)
    print(f"TOTAL       : {total:8.2f} kg CO2")
    print("="*55)

    # Simple evaluation
    if total < 300:
        level = "Excellent (Very Low)"
    elif total < 600:
        level = "Good"
    elif total < 1000:
        level = "Average - Can Improve"
    else:
        level = "High - Action Needed"

    print(f"\nYour level: {level}")

    print("\n--- Tips to Reduce Your Carbon Footprint ---")
    print("1. Switch to LED bulbs and unplug unused devices.")
    print("2. Use public transport, carpool, or bicycle more.")
    print("3. Reduce meat consumption and food waste.")
    print("4. Recycle and compost organic waste.")
    print("5. Consider renewable energy options if possible.")
    print("="*55)

def main():
    """Main function - controls the application flow"""
    # Initialize emission values
    electricity = 0.0
    transport = 0.0
    food = 0.0
    waste = 0.0

    print("\nWelcome to Personal Carbon Footprint Calculator!")
    print("This tool helps you understand and reduce your impact on climate.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            electricity = calculate_electricity()
        elif choice == '2':
            transport = calculate_transport()
        elif choice == '3':
            food = calculate_food()
        elif choice == '4':
            waste = calculate_waste()
        elif choice == '5':
            show_results(electricity, transport, food, waste)
        elif choice == '6':
            electricity = transport = food = waste = 0.0
            print("\nAll data has been reset.")
        elif choice == '7':
            print("\nThank you for using the Carbon Footprint Calculator!")
            print("Together we can fight climate change. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select a number between 1 and 7.")

# Run the application
if __name__ == "__main__":
    main()