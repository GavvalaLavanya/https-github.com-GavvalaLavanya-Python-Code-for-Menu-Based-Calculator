while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting the program.")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        result = a + b
        print("Result:", result)
    elif choice == 2:
        result = a - b
        print("Result:", result)
    elif choice == 3:
        result = a * b
        print("Result:", result)
    elif choice == 4:
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = a / b
            print("Result:", result)
    else:
        print("Invalid choice. Please select from 1 to 5.")
