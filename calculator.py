class CarbonCalculator:
    def __init__(self):
        self.factors = {
            "car": 0.21,
            "motorcycle": 0.11,
            "bus": 0.05,
            "train": 0.04,
            "electricity": 0.55,
            "meat": 2.5,
            "vegetarian": 0.8,
            "vegan": 0.4,
            "waste": 0.5
        }

        # Multiple transport
        self.car_km = 0
        self.motorcycle_km = 0
        self.bus_km = 0
        self.train_km = 0

        self.electricity = 0
        self.meat_meals = 0
        self.veg_meals = 0
        self.vegan_meals = 0
        self.waste = 0