Malaysian Tax Calculator

📌 Overview

This project is a Python-based Malaysian income tax calculator that allows users to register, log in, and compute their tax payable based on annual income and tax relief.

The system stores user data and tax records using CSV files, enabling users to track their past tax calculations.


🎯 Problem Statement

Manual tax calculation can be complex and prone to errors, especially when dealing with multiple income brackets and reliefs. This project provides a simple automated solution to calculate Malaysian income tax accurately and efficiently.


⚙️ Features

* User registration and login (IC-based authentication)
* Income tax calculation using progressive tax rates
* Store tax records in CSV files
* View past tax calculation history
* Input validation for better user experience
  

🛠️ Technologies Used

* Python
* Pandas (data handling)
* CSV (data storage)



🧠 Tax Calculation Logic

The system calculates tax based on **chargeable income**:

> Chargeable Income = Income – Tax Relief

Then applies Malaysian progressive tax rates to determine tax payable.



📂 Project Structure

malaysia-tax-calculator/
│
├── data/
│   ├── users.csv
│   └── tax_records.csv
│
├── src/
│   ├── main.py
│   └── functions.py
│
├── README.md



🚀 How to Run

1. Install required library:

pip install pandas


2. Run the program:

python main.py


3. Follow the steps:

* Enter IC number
* Register or login
* Input income & tax relief
* View tax results


📊 Example Output


--- TAX SUMMARY ---
Chargeable Income       : RM35,000.00
Tax Payable             : RM600.00



💡 Future Improvements

* Add graphical user interface (GUI)
* Integrate real Malaysian tax API/rules
* Convert into web application (Streamlit / Flask)
* Improve security (hashed passwords)



👩‍💻 Author

Siti Sarah binti Mohd Affandi



📌 Notes

This project is developed as part of academic coursework and enhanced for portfolio purposes.
