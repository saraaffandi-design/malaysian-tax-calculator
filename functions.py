import pandas as pd
import os

# === Verify user based on IC and optional password ===
def verify_user(ic_number, password=None, filename="users.csv"):
    """
    Verify a user's IC number and optional password.
    Returns the user record as a dictionary if valid, otherwise None.
    """
    if len(ic_number) != 12 or not ic_number.isdigit():
        return None

    if not os.path.exists(filename):
        return None

    df = pd.read_csv(filename)
    user_row = df[df["IC"].astype(str) == str(ic_number)]

    if user_row.empty:
        return None

    user = user_row.iloc[0].to_dict()

    # If password is given, check last 4 digits or stored password
    if password is not None:
        last4 = str(ic_number)[-4:]
        if password != last4 and password != str(user["Password"]):
            return None

    return user


# === Register new user ===
def register_user(ic_number, user_id, password, filename="users.csv"):
    """
    Register a new user by saving IC, User ID, and password to users.csv.
    Creates the file if it doesn't exist.
    """
    if os.path.exists(filename):
        df = pd.read_csv(filename)
    else:
        df = pd.DataFrame(columns=["IC", "UserID", "Password"])

    new_user = {"IC": ic_number, "UserID": user_id, "Password": password}
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_csv(filename, index=False)


# === Tax calculation ===
def calculate_tax(income, relief):
    """
    Calculate Malaysian income tax payable based on annual income and relief.
    Returns a dictionary with chargeable income and tax.
    """
    taxable_income = income - relief
    if taxable_income <= 0:
        return {"chargeable_income": taxable_income, "tax": 0.0}

    # Progressive tax calculation
    if taxable_income <= 5000:
        tax = 0
    elif taxable_income <= 20000:
        tax = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax = 150 + (taxable_income - 20000) * 0.03
    elif taxable_income <= 50000:
        tax = 600 + (taxable_income - 35000) * 0.06
    elif taxable_income <= 70000:
        tax = 1500 + (taxable_income - 50000) * 0.11
    elif taxable_income <= 100000:
        tax = 3700 + (taxable_income - 70000) * 0.19
    elif taxable_income <= 250000:
        tax = 9400 + (taxable_income - 100000) * 0.25
    elif taxable_income <= 400000:
        tax = 46900 + (taxable_income - 250000) * 0.26
    else:
        tax = 85900 + (taxable_income - 400000) * 0.28

    return {"chargeable_income": taxable_income, "tax": tax}


# === Save tax record to CSV ===
def save_to_csv(data, filename="tax_records.csv"):
    """
    Save user's tax calculation data to a CSV file.
    Appends new rows if file already exists.
    """
    df = pd.DataFrame([data])
    if os.path.exists(filename):
        df.to_csv(filename, mode="a", header=False, index=False)
    else:
        df.to_csv(filename, index=False)


# === Read and display current user's CSV records ===
def read_from_csv(ic_number, filename="tax_records.csv"):
    """
    Read and display saved tax records for the current user only.
    Returns the user's DataFrame if exists, else None.
    """
    import pandas as pd
    import os

    if not os.path.exists(filename):
        print("⚠️ No tax records found yet.")
        return None

    df = pd.read_csv(filename)
    user_df = df[df["IC"].astype(str) == str(ic_number)]

    if user_df.empty:
        print("⚠️ No tax records found for this user.")
        return None

    print("\n=== Your Tax Records ===")
   
    # Show only key columns in a cleaner table
    
    print(
        user_df[["Income", "TaxRelief", "ChargeableIncome", "TaxPayable"]]
        .to_string(index=False)
    )

    print(
        f"\n📊 You have {len(user_df)} past record(s). "
        f"Latest tax payable: RM{user_df['TaxPayable'].iloc[-1]:,.2f}"
    )

    return user_df

