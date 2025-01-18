def convert(feet, choice):
    conversions = [
        feet * 12,    
        feet / 3,    
        feet / 5280, 
        feet * 304.8,      
        feet * 30.48,      
        feet * 0.3048,
        feet * 0.0003048   
    ]
    return conversions[choice - 1]

def main():
    feet = float(input("Enter a length in feet: "))
    print("\nChoose the conversion option:")
    print("1. Convert to inches")
    print("2. Convert to yards")
    print("3. Convert to miles")
    print("4. Convert to millimeters")
    print("5. Convert to centimeters")
    print("6. Convert to meters")
    print("7. Convert to kilometers")
    choice = int(input("\nEnter the number of your choice: "))
    
    if 1 <= choice <= 7:
        result = convert(feet, choice)
        print(f"\nThe conversion result is: {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
main()
