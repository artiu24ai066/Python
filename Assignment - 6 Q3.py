class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()
        self.conversion_factors = {
            'inches': 1,
            'feet': 1/12,
            'yards': 1/36,
            'miles': 1/63360,
            'kilometers': 1/39370.1,
            'meters': 1/39.3701,
            'centimeters': 2.54,
            'millimeters': 25.4
        }

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Invalid target unit: {target_unit}")

        length_in_inches = self.length * self.conversion_factors[self.unit]
        target_length = length_in_inches * self.conversion_factors[target_unit]
        return target_length

    def inches(self):
        return self.convert_to('inches')

    def feet(self):
        return self.convert_to('feet')

    def yards(self):
        return self.convert_to('yards')

    def miles(self):
        return self.convert_to('miles')

    def kilometers(self):
        return self.convert_to('kilometers')

    def meters(self):
        return self.convert_to('meters')

    def centimeters(self):
        return self.convert_to('centimeters')

    def millimeters(self):
        return self.convert_to('millimeters')

length = float(input("Enter the length: "))
unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()

c = Converter(length, unit)

print("\nSelect a unit to convert to:")
print("1. Inches")
print("2. Feet")
print("3. Yards")
print("4. Miles")
print("5. Kilometers")
print("6. Meters")
print("7. Centimeters")
print("8. Millimeters")

choice = int(input("Enter your choice (1-8): "))

if choice == 1:
    print(f"{length} {unit} is {c.inches()} inches")
elif choice == 2:
    print(f"{length} {unit} is {c.feet()} feet")
elif choice == 3:
    print(f"{length} {unit} is {c.yards()} yards")
elif choice == 4:
    print(f"{length} {unit} is {c.miles()} miles")
elif choice == 5:
    print(f"{length} {unit} is {c.kilometers()} kilometers")
elif choice == 6:
    print(f"{length} {unit} is {c.meters()} meters")
elif choice == 7:
    print(f"{length} {unit} is {c.centimeters()} centimeters")
elif choice == 8:
    print(f"{length} {unit} is {c.millimeters()} millimeters")
else:
    print("Invalid choice!")
