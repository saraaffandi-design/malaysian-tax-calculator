from functions import verify_user, register_user, calculate_tax, save_to_csv, read_from_csv

print(" MALAYSIAN TAX CALCULATOR \n")

while True:
    ic_number = input("Enter your 12-digit IC number (or 'exit' to quit): ")

    if ic_number.lower() == "exit":
        print("Goodbye!")
        break

    # Validate IC number
    if len(ic_number) != 12 or not ic_number.isdigit():
        print("❌ Invalid IC number. Please enter again.\n")
        continue

    # Check if user already registered
    user = verify_user(ic_number)

    if user is None:
        # Not registered
        print("You are not registered yet. Please register first.")
        user_id = input("Create your User ID: ")
        password = input("Set your password (last 4 digits of IC recommended): ")

        # Register new user
        register_user(ic_number, user_id, password)
        print("✅ Registration successful!\n")
        print("Now please log in to continue.\n")
    
    else:
        # Already registered
        print("✅ User already registered!")
        print("Now please log in to continue.\n")

    # Proceed to login
    logged_in = False
    while not logged_in:
        entered_user_id = input("Enter your User Id: ")
        entered_password = input("Enter your password: ")

        # Verify again using password logic
        user = verify_user(ic_number, entered_password)
        if user is not None and user["UserID"] == entered_user_id:
            print(f"\n=== Welcome, {entered_user_id}! ===")
            logged_in = True
        else:
            print("❌ Invalid login credentials. Please try again.\n")

    # Tax calculation
    while True:
        try:
            income = float(input("Enter your annual income (RM): "))
            relief = float(input("Enter your total tax relief (RM): "))
            break
        except ValueError:
            print("❌ Please enter valid numeric values.\n")

    # Calculate and display tax
    result = calculate_tax(income, relief)
    print("\n--- TAX SUMMARY ---")
    print(f"{'Chargeable Income':<25}: RM{result['chargeable_income']:,.2f}")
    print(f"{'Tax Payable':<25}: RM{result['tax']:,.2f}\n")

    # Save record
    save_to_csv({
        "IC": ic_number,
        "UserID": user["UserID"],
        "Income": income,
        "TaxRelief": relief,
        "ChargeableIncome": result["chargeable_income"],
        "TaxPayable": result["tax"]
    })

    # Option to view current user's tax records
    view = input("Would you like to view your saved tax records? (y/n): ").lower()
    if view == "y":
        read_from_csv(ic_number)

    cont = input("\nDo you want to calculate again? (y/n): ").lower()
    if cont != "y":
        print("Thank you for using the Malaysian Tax Calculator!")
        break
