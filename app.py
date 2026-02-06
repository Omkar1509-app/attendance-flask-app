from flask import Flask, render_template, request
import pandas as pd
from datetime import date

app = Flask(__name__)

def load_data():
    df = pd.read_excel("Attendance.xlsx")
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    return df

@app.route("/", methods=["GET", "POST"])
def index():
    employees = []
    shift = None
    today = date.today()

    if request.method == "POST":
        shift = request.form.get("shift")
        data = load_data()

        present_employees = data[
            (data['Date'] == today) &
            (data['Shift'] == shift) &
            (data['Status'] == 'Present')
        ]

        employees = present_employees['Name'].tolist()

    return render_template(
        "index.html",
        employees=employees,
        shift=shift,
        today=today
)

if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000, debug=True)