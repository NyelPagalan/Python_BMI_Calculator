while True:
    try:
        # User input for height and weight
        print("===================================")
        print("  Welcome to the BMI Calculator")
        print("===================================")

        height = float(input("Enter your height in meters (e.g., 1.54): "))
        weight = float(input("Enter your weight in kilograms (e.g., 45): "))

        # Checks if input is valid
        if height <= 0 or weight <= 0:
            print("Please enter a valid number")
            continue

        # Formula or calculations to get the BMI
        bmi = weight / (height ** 2)

        # Category based on BMI values
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Output
        print(f"Your BMI is {bmi:.1f}")
        print(f"Your category is {category}")

        break

    except ValueError:
        print("Please enter a number")
        continue