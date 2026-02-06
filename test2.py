import pandas as pd
from datetime import date

# Read Excel file
data = pd.read_excel("Untitled 1.xlsx")

# Convert Date column to date
data['Date'] = pd.to_datetime(data['Date']).dt.date

today = date.today()

shift = input("Enter shift (A/B/C/D): ").upper()

present_employees = data[
(data['Date'] == today) &
(data['Shift'] == shift) &
(data['Status'] == 'Present')
]

if present_employees.empty:
     print(f"No employees present in Shift {shift} today.")
else:
     print(f"Employees Present Today - Shift {shift}")
for name in present_employees['Name']:
        print(name)