def show_tips(transport_co2, electricity_co2, food_co2, waste_co2):
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
    print(f"{BOLD}{CYAN}        WHAT YOU SHOULD DO (TIPS){RESET}")
    print("=" * 55)

    sources = {
        "Transportation": transport_co2,
        "Electricity": electricity_co2,
        "Food": food_co2,
        "Waste": waste_co2
    }
    highest = max(sources, key=sources.get)

    print(f"{YELLOW}Your highest emission is from: {BOLD}{highest}{RESET}\n")

    if highest == "Transportation":
        print(f"{GREEN}→{RESET} Try to use public transport more often")
        print(f"{GREEN}→{RESET} Carpool with friends or colleagues")
        print(f"{GREEN}→{RESET} Walk or cycle for short distances")
        print(f"{GREEN}→{RESET} Reduce private car usage when possible")
    elif highest == "Electricity":
        print(f"{GREEN}→{RESET} Switch off lights and fans when leaving room")
        print(f"{GREEN}→{RESET} Use LED bulbs instead of normal bulbs")
        print(f"{GREEN}→{RESET} Unplug chargers when not in use")
        print(f"{GREEN}→{RESET} Use fan instead of air-conditioner when possible")
    elif highest == "Food":
        print(f"{GREEN}→{RESET} Reduce meat meals, try more vegetables")
        print(f"{GREEN}→{RESET} Don't waste food")
        print(f"{GREEN}→{RESET} Plan your meals before cooking")
        print(f"{GREEN}→{RESET} Support local and seasonal food")
    else:
        print(f"{GREEN}→{RESET} Separate plastic, paper and food waste")
        print(f"{GREEN}→{RESET} Reduce single-use plastic")
        print(f"{GREEN}→{RESET} Reuse bags and containers")
        print(f"{GREEN}→{RESET} Try composting food waste if possible")

    print(f"\n{BOLD}{BLUE}General Advice:{RESET}")
    print(f"{MAGENTA}→{RESET} Small daily changes can reduce your carbon footprint a lot.")
    print(f"{MAGENTA}→{RESET} Try to improve your Eco Score step by step.")
    print("=" * 55)