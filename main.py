import calculator

while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
 
    choice = input("Enter Choice: ")

    if choice == "5":
        print("Calculator Closed")
        break

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Result =", calculator.add(num1, num2))

    elif choice == "2":
        print("Result =", calculator.sub(num1, num2))

    elif choice == "3":
        print("Result =", calculator.mul(num1, num2))

    elif choice == "4":
        print("Result =", calculator.div(num1, num2))

    else:
        print("Invalid Choice")