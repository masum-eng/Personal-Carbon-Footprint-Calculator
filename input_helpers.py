def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter 0 or positive number.")
            else:
                return value
        except:
            print("Invalid input. Please enter a number.")


def get_int(prompt, minimum=0, maximum=20):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum or value > maximum:
                print(f"Please enter between {minimum} and {maximum}.")
            else:
                return value
        except:
            print("Invalid input. Please enter whole number.")
            