from input_helpers import get_number, get_int

def collect_data(calc):
    # Color codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    RED = "\033[91m"

    print("\n" + "=" * 55)
    print(f"{BOLD}{CYAN}   PERSONAL CARBON FOOTPRINT CALCULATOR{RESET}")
    print(f"{BOLD}{YELLOW}          SDG 13 - Climate Action{RESET}")
    print("=" * 55)
    print(f"{WHITE}Please answer the following questions one by one.{RESET}\n")

    # 1. Transportation
    print(f"{BOLD}{BLUE}--- 1. Transportation ---{RESET}")
    print(f"{GREEN}You can enter multiple transport types.{RESET}")
    print(f"{GREEN}If you did not use any, just type 0.{RESET}\n")

    calc.car_km = get_number(f"{YELLOW}Car (km): {RESET}")
    calc.motorcycle_km = get_number(f"{YELLOW}Motorcycle (km): {RESET}")
    calc.bus_km = get_number(f"{YELLOW}Bus (km): {RESET}")
    calc.train_km = get_number(f"{YELLOW}Train / LRT / MRT (km): {RESET}")

    # 2. Electricity
    print(f"\n{BOLD}{BLUE}--- 2. Electricity Usage ---{RESET}")
    calc.electricity = get_number(f"{YELLOW}How many kWh electricity did you use today? {RESET}")

    # 3. Food
    print(f"\n{BOLD}{BLUE}--- 3. Food Consumption ---{RESET}")
    print(f"{GREEN}How many meals did you eat today?{RESET}")
    calc.meat_meals = get_int(f"{YELLOW}Meat-based meals: {RESET}")
    calc.veg_meals = get_int(f"{YELLOW}Vegetarian meals: {RESET}")
    calc.vegan_meals = get_int(f"{YELLOW}Vegan meals: {RESET}")

    # 4. Waste
    print(f"\n{BOLD}{BLUE}--- 4. Waste ---{RESET}")
    calc.waste = get_number(f"{YELLOW}Approximate waste you produced today (kg): {RESET}")

    print(f"\n{BOLD}{GREEN}All data collected successfully!{RESET}")