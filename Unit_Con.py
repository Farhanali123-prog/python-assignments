def convert_units():
    print("Welcome to the Unit Conversion Calculator!")
    print("Choose a conversion type:")
    print("1. Kilometers to Meters")
    print("2. Minutes to Seconds")
    print("3. Hours to Minutes")
    print("4. Grams to Kilograms")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            km = float(input("Enter distance in kilometers: "))
            print(f"{km} kilometers is {km * 1000} meters.")
        elif choice == '2':
            mins = float(input("Enter time in minutes: "))
            print(f"{mins} minutes is {mins * 60} seconds.")
        elif choice == '3':
            hours = float(input("Enter time in hours: "))
            print(f"{hours} hours is {hours * 60} minutes.")
        elif choice == '4':
            grams = float(input("Enter weight in grams: "))
            print(f"{grams} grams is {grams / 1000} kilograms.")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

convert_units()
