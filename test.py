import pandas as pd

from datetime import date


# Load Excel file

data = pd.read_excel("Untitled 1.xlsx")


# Get today's date

today = date.today()


# Take shift input from user

shift = input("Enter shift (A/B/C/D): ").upper()


# Filter data

present_employees = data[

    (data['Date'] == today) &

    (data['Shift'] == shift) &

    (data['Status'] == 'Present')

]


# Display result

if present_employees.empty:

    print(f"No employees present in Shift {shift} today.")

else:

    print(f"Employees Present Today – Shift {shift}")

    for name in present_employees['Name']:

        print(name)