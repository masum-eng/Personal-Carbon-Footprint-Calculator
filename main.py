from calculator import CarbonCalculator
from data_collector import collect_data
from calculator_engine import calculate_and_show

def main():
    print("Welcome to Personal Carbon Footprint Calculator!")
    print("I will ask you some questions one by one.")
    print("After you answer everything, I will calculate and give tips automatically.\n")

    while True:
        calc = CarbonCalculator()
        collect_data(calc)
        calculate_and_show(calc)

        print("\nDo you want to calculate again?")
        again = input("Type 'yes' to continue or 'no' to exit: ").lower().strip()

        if again != "yes" and again != "y":
            print ("\nThank you for using this calculator!")
            print("Every small action counts for Climate Action (SDG 13).")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()